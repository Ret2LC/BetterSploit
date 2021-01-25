#!/bin/bash

FILE=$1

function audit_code()
{
    # THERE ARE DUPES HERE BECUASE I HAD TO RE DO THE WANTED SYNTAX
    cat  $FILE | grep --line-buffered --line-number -i 'devnull\|sync\|removedirs\|openpty\|fdopen\|check_output\|args\|/bin/bash\|\|/bin/sh\|\|tty\|tty.spawn\|Popen\|stderr\|STDERR\|pipe\|PIPE\|STDOUT\|stdout\|run\|os.spawn\|shell_exec\|database\|db\|SELECT\|FROM\|return\|strcpy\|vsprintf\|gets\|strncpy\|strcpy\|strcat\|strncat\|snprintf\|fgets\|strlen\|scanf\|dll\|fscan>\|accept\|listen\|connect\|SELECT\|FROM\|system\|syscall\|return\|os.system\|subproccess\|os\|popen\|exec\|shell=True\|api\|SELECT\|FROM\|cmd\|syscall\|system\|config\|dll\|api\|SELECT\|FROM\|buffer\|BUFFER\|buf\|BUF\|buffer_size\|BUFFER_SIZE\|syscall\|system\|constantize\|dll\|listen\|rend\|SELECT\|FROM\|apache_child_terminate\|apache_setenv\|define_syslog_variables\|escapeshellarg\|escapeshellcmd\|eval\|exec'
}

audit_code
