#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║         MYTERMUX PYTHON EDITION - RICH UI                   ║
║         Developer: Ari Marshello                            ║
╚══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import shutil
import subprocess
import platform
import datetime
from pathlib import Path

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.align import Align
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.prompt import Prompt, Confirm
from rich.box import ROUNDED, HEAVY, DOUBLE

console = Console()
HOME = Path.home()
TERMUX_DIR = HOME / ".termux"
BACKUP_DIR = HOME / ".mytermux_backup"
DEVELOPER = "Ari Marshello"


def clear():
    os.system('clear')


def jalankan(cmd, tampilkan=False):
    try:
        if tampilkan:
            return subprocess.run(cmd, shell=True).returncode == 0
        return subprocess.run(cmd, shell=True,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
    except:
        return False


def ada_command(cmd):
    return shutil.which(cmd) is not None


def backup_file(path):
    if not path.exists():
        return
    BACKUP_DIR.mkdir(exist_ok=True)
    ts = int(time.time())
    dst = BACKUP_DIR / f"{path.name}_{ts}.bak"
    shutil.copy(path, dst)
    console.print(f"  [dim]Backup: {dst.name}[/dim]")


def pause(msg="Tekan Enter untuk kembali..."):
    console.print()
    Prompt.ask(f"[dim]{msg}[/dim]", default="", show_default=False)


def banner():
    logo = """[bold cyan]
    ███╗   ███╗██╗   ██╗████████╗███████╗██████╗ ███╗   ███╗██╗   ██╗██╗  ██╗
    ████╗ ████║╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║   ██║╚██╗██╔╝
    ██╔████╔██║ ╚████╔╝    ██║   █████╗  ██████╔╝██╔████╔██║██║   ██║ ╚███╔╝ 
    ██║╚██╔╝██║  ╚██╔╝     ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║ ██╔██╗ 
    ██║ ╚═╝ ██║   ██║      ██║   ███████╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██╔╝ ██╗
    ╚═╝     ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝[/bold cyan]"""

    sub = f"[bold yellow]PYTHON EDITION with RICH UI[/bold yellow]"
    dev = f"[bold bright_magenta]Developer: {DEVELOPER}[/bold bright_magenta]"

    content = f"{logo}\n\n{Align.center(sub)}\n{Align.center(dev)}"

    console.print(Panel(
        Align.center(content),
        border_style="bright_magenta",
        box=DOUBLE,
        padding=(1, 2),
    ))


TEMA = {
    "1":  ("Dracula",          "#282a36", "#f8f8f2", "#bd93f9", "#ff79c6", "#50fa7b", "#f1fa8c", "#8be9fd", "#ff5555", "magenta"),
    "2":  ("Gruvbox Dark",     "#282828", "#ebdbb2", "#d79921", "#b16286", "#98971a", "#fabd2f", "#689d6a", "#cc241d", "yellow"),
    "3":  ("Tokyo Night",      "#1a1b26", "#c0caf5", "#7aa2f7", "#bb9af7", "#9ece6a", "#e0af68", "#7dcfff", "#f7768e", "blue"),
    "4":  ("Nord",             "#2e3440", "#d8dee9", "#88c0d0", "#b48ead", "#a3be8c", "#ebcb8b", "#81a1c1", "#bf616a", "cyan"),
    "5":  ("Cyberpunk Neon",   "#000000", "#00ff9c", "#00b8ff", "#ff00ff", "#00ff9c", "#fffc00", "#00ffff", "#ff003c", "green"),
    "6":  ("Material Ocean",   "#0f111a", "#a6accd", "#82aaff", "#c792ea", "#c3e88d", "#ffcb6b", "#89ddff", "#f07178", "blue"),
    "7":  ("Matrix Green",     "#000000", "#00ff00", "#00ff00", "#00cc00", "#00ff00", "#ccff00", "#00ffff", "#ff0000", "green"),
    "8":  ("Pink Sweet",       "#1a0b1e", "#ffd6e8", "#c77dff", "#ff69b4", "#ffa8c5", "#ffd97d", "#a2d2ff", "#ff4d6d", "magenta"),
    "9":  ("Monokai Pro",      "#2d2a2e", "#fcfcfa", "#78dce8", "#ab9df2", "#a9dc76", "#ffd866", "#78dce8", "#ff6188", "yellow"),
    "10": ("Catppuccin Mocha", "#1e1e2e", "#cdd6f4", "#89b4fa", "#cba6f7", "#a6e3a1", "#f9e2af", "#94e2d5", "#f38ba8", "magenta"),
}


def buat_colors(nama, bg, fg, w1, w2, w3, w4, w5, err):
    return f"""background={bg}
foreground={fg}
cursor={w1}

color0={bg}
color1={err}
color2={w3}
color3={w5}
color4={w1}
color5={w2}
color6={w4}
color7={fg}
color8=#555555
color9={err}
color10={w3}
color11={w5}
color12={w1}
color13={w2}
color14={w4}
color15=#ffffff
"""


def buat_zshrc():
    zshrc_path = HOME / ".zshrc"
    backup_file(zshrc_path)

    content = r'''# MYTERMUX ZSHRC - Developer: Ari Marshello

export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME="powerlevel10k/powerlevel10k"

plugins=(
    git
    zsh-autosuggestions
    zsh-syntax-highlighting
    zsh-completions
    colored-man-pages
    command-not-found
    extract
    sudo
    history-substring-search
)

source $ZSH/oh-my-zsh.sh

alias ls='eza --icons --group-directories-first 2>/dev/null || ls --color=auto'
alias ll='eza -lah --icons --group-directories-first 2>/dev/null || ls -lah'
alias la='eza -A --icons --group-directories-first 2>/dev/null || ls -A'
alias lt='eza --tree --level=2 --icons'
alias cat='bat --style=plain 2>/dev/null || cat'
alias grep='grep --color=auto'
alias cls='clear'
alias c='clear'
alias ..='cd ..'
alias ...='cd ../..'
alias py='python'
alias update='pkg update && pkg upgrade -y'
alias mytermux='python ~/mytermux.py'

eval "$(zoxide init zsh)" 2>/dev/null
alias cd='z'

HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=10000
setopt SHARE_HISTORY
setopt HIST_IGNORE_ALL_DUPS
setopt HIST_IGNORE_SPACE

if [ -f ~/.mytermux_welcome ]; then
    python ~/mytermux.py --welcome
fi

[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
'''
    with open(zshrc_path, 'w') as f:
        f.write(content)

    p10k_content = r'''typeset -g POWERLEVEL9K_LEFT_PROMPT_ELEMENTS=(dir vcs newline prompt_char)
typeset -g POWERLEVEL9K_RIGHT_PROMPT_ELEMENTS=(status command_execution_time time)
typeset -g POWERLEVEL9K_MODE=nerdfont-complete
typeset -g POWERLEVEL9K_PROMPT_CHAR_OK_{VIINS,VICMD,VIVIS,VIOWR}_FOREGROUND=76
typeset -g POWERLEVEL9K_PROMPT_CHAR_ERROR_{VIINS,VICMD,VIVIS,VIOWR}_FOREGROUND=196
typeset -g POWERLEVEL9K_PROMPT_CHAR_{OK,ERROR}_VIINS_CONTENT_EXPANSION='❯'
typeset -g POWERLEVEL9K_DIR_FOREGROUND=39
typeset -g POWERLEVEL9K_VCS_CLEAN_FOREGROUND=76
typeset -g POWERLEVEL9K_VCS_MODIFIED_FOREGROUND=178
typeset -g POWERLEVEL9K_TIME_FOREGROUND=66
typeset -g POWERLEVEL9K_TIME_FORMAT='%D{%H:%M:%S}'
typeset -g POWERLEVEL9K_STATUS_OK=false
'''
    with open(HOME / ".p10k.zsh", 'w') as f:
        f.write(p10k_content)

    console.print(f"  [bright_green]✓[/bright_green] [dim].zshrc dan .p10k.zsh dibuat[/dim]")


def install_zsh_silent():
    steps = [
        ("Update package", "pkg update -y"),
        ("Install git, zsh, curl", "pkg install -y git zsh curl wget"),
        ("Install tools keren", "pkg install -y fzf bat eza zoxide"),
    ]

    with Progress(
        SpinnerColumn(style="bright_cyan"),
        TextColumn("[bold]{task.description}"),
        BarColumn(complete_style="bright_green"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Memulai...", total=len(steps) + 6)

        for desc, cmd in steps:
            progress.update(task, description=f"[cyan]{desc}")
            jalankan(cmd)
            progress.advance(task)

        zsh_path = shutil.which('zsh')
        if zsh_path:
            jalankan(f"chsh -s {zsh_path}")
        progress.advance(task)

        omz = HOME / ".oh-my-zsh"
        if not omz.exists():
            progress.update(task, description="[cyan]Install Oh My Zsh")
            jalankan('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended')
        progress.advance(task)

        plugins = omz / "custom" / "plugins"
        themes = omz / "custom" / "themes"
        plugins.mkdir(parents=True, exist_ok=True)
        themes.mkdir(parents=True, exist_ok=True)

        for nama, path, url in [
            ("Powerlevel10k", themes / "powerlevel10k", "https://github.com/romkatv/powerlevel10k.git"),
            ("zsh-autosuggestions", plugins / "zsh-autosuggestions", "https://github.com/zsh-users/zsh-autosuggestions.git"),
            ("zsh-syntax-highlighting", plugins / "zsh-syntax-highlighting", "https://github.com/zsh-users/zsh-syntax-highlighting.git"),
            ("zsh-completions", plugins / "zsh-completions", "https://github.com/zsh-users/zsh-completions.git"),
        ]:
            progress.update(task, description=f"[cyan]Install {nama}")
            if not path.exists():
                jalankan(f'git clone --depth=1 "{url}" "{path}"')
            progress.advance(task)

        progress.update(task, description="[cyan]Buat konfigurasi")
        buat_zshrc()
        progress.advance(task)


def install_zsh():
    clear()
    banner()

    info = Table(show_header=False, box=None, padding=(0, 2))
    info.add_column(style="bright_green")
    info.add_column(style="white")

    info.add_row("✓", "ZSH")
    info.add_row("✓", "Oh My Zsh")
    info.add_row("✓", "Powerlevel10k")
    info.add_row("✓", "zsh-autosuggestions")
    info.add_row("✓", "zsh-syntax-highlighting")
    info.add_row("✓", "zsh-completions")
    info.add_row("✓", "fzf, bat, eza, zoxide")

    console.print(Panel(
        info,
        title="[bold cyan]Paket[/bold cyan]",
        border_style="cyan",
        box=ROUNDED,
        padding=(1, 2),
    ))

    console.print(Panel(
        f"[bold yellow]Developer: {DEVELOPER}[/bold yellow]",
        border_style="yellow",
        box=ROUNDED,
    ))
    console.print()

    if not Confirm.ask("[bold bright_green]Lanjut install?[/bold bright_green]", default=False):
        console.print("\n[yellow]Dibatalkan.[/yellow]")
        pause()
        return

    install_zsh_silent()

    console.print()
    console.print(Panel(
        f"[bold bright_green]INSTALASI SELESAI[/bold bright_green]\n\n"
        f"[yellow]Restart Termux atau ketik:[/yellow] [bold white]exec zsh[/bold white]\n"
        f"[yellow]Pilih opsi[/yellow] [bold white]1[/bold white]\n\n"
        f"[dim]Developer: {DEVELOPER}[/dim]",
        border_style="bright_green",
        box=DOUBLE,
        padding=(1, 2),
    ))
    pause()


def ganti_warna():
    while True:
        clear()
        banner()

        table = Table(
            title="[bold bright_magenta]DAFTAR TEMA WARNA[/bold bright_magenta]",
            box=HEAVY,
            border_style="bright_magenta",
            header_style="bold bright_cyan",
            show_lines=True,
            padding=(0, 1),
        )
        table.add_column("No", style="bold yellow", justify="center", width=4)
        table.add_column("Nama Tema", style="bold white", width=20)
        table.add_column("Preview", justify="center", width=25)
        table.add_column("Warna", justify="center", width=30)

        for k, tema in TEMA.items():
            nama, bg, fg, w1, w2, w3, w4, w5, err, warna_rich = tema
            preview = f"[on {bg}]  [/on {bg}]  [white]│[/white]  [{warna_rich}]████[/{warna_rich}]"
            warna_hex = f"[{warna_rich}]{bg}[/{warna_rich}] [dim]{fg}[/dim]"
            table.add_row(
                f"[bold yellow]{k}[/bold yellow]",
                f"[bold]{nama}[/bold]",
                preview,
                warna_hex,
            )

        console.print(table)
        console.print()

        console.print(Panel(
            "[bold bright_red][0][/bold bright_red] Kembali    "
            "[bold bright_green][R][/bold bright_green] Reset",
            border_style="dim",
            box=ROUNDED,
        ))
        console.print()

        pilih = Prompt.ask(
            "[bold bright_magenta]➜ Pilih tema[/bold bright_magenta]",
            default="0"
        ).strip().upper()

        if pilih == '0':
            return
        elif pilih == 'R':
            prop = TERMUX_DIR / "colors.properties"
            if prop.exists():
                backup_file(prop)
                prop.unlink()
                jalankan("termux-reload-settings")
                console.print("\n[bold bright_green]Tema direset[/bold bright_green]")
            else:
                console.print("\n[bold yellow]Tidak ada tema[/bold yellow]")
            time.sleep(1.5)
        elif pilih in TEMA:
            nama = TEMA[pilih][0]
            tema = TEMA[pilih]
            content = buat_colors(tema[0], tema[1], tema[2], tema[3], tema[4], tema[5], tema[6], tema[7], tema[8])

            TERMUX_DIR.mkdir(exist_ok=True)
            prop = TERMUX_DIR / "colors.properties"
            if prop.exists():
                backup_file(prop)

            with open(prop, 'w') as f:
                f.write(content)

            jalankan("termux-reload-settings")
            console.print()
            console.print(Panel(
                f"[bold bright_green]Tema '{nama}' dipasang[/bold bright_green]\n\n"
                f"[dim]Developer: {DEVELOPER}[/dim]",
                border_style="bright_green",
                box=DOUBLE,
            ))
            time.sleep(2)
        else:
            console.print(f"\n[bold bright_red]Pilihan tidak valid[/bold bright_red]")
            time.sleep(1)


FONTS = {
    "1": ("JetBrains Mono", "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/JetBrainsMono/Ligatures/Regular/JetBrainsMonoNerdFont-Regular.ttf"),
    "2": ("Fira Code", "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/FiraCode/Regular/FiraCodeNerdFont-Regular.ttf"),
    "3": ("Hack", "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/Hack/Regular/HackNerdFont-Regular.ttf"),
    "4": ("Cascadia Code", "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/CascadiaCode/Regular/CascadiaCodeNF-Regular.ttf"),
    "5": ("Ubuntu Mono", "https://github.com/ryanoasis/nerd-fonts/raw/master/patched-fonts/UbuntuMono/Regular/UbuntuMonoNerdFont-Regular.ttf"),
    "6": ("MesloLGS NF", "https://github.com/romkatv/powerlevel10k-media/raw/master/MesloLGS%20NF%20Regular.ttf"),
}


def ganti_font():
    while True:
        clear()
        banner()

        table = Table(
            title="[bold bright_cyan]DAFTAR FONT[/bold bright_cyan]",
            box=HEAVY,
            border_style="bright_cyan",
            header_style="bold bright_yellow",
            show_lines=True,
        )
        table.add_column("No", style="bold yellow", justify="center", width=4)
        table.add_column("Nama Font", style="bold white", width=20)

        for k, (nama, _) in FONTS.items():
            table.add_row(f"[bold yellow]{k}[/bold yellow]", f"[bold]{nama}[/bold]")

        console.print(table)
        console.print()
        console.print(Panel(
            "[bold bright_red][0][/bold bright_red] Kembali    "
            "[bold bright_green][R][/bold bright_green] Reset",
            border_style="dim",
            box=ROUNDED,
        ))
        console.print()

        pilih = Prompt.ask("[bold bright_cyan]➜ Pilih font[/bold bright_cyan]", default="0").strip().upper()

        if pilih == '0':
            return
        elif pilih == 'R':
            font = TERMUX_DIR / "font.ttf"
            if font.exists():
                backup_file(font)
                font.unlink()
                jalankan("termux-reload-settings")
                console.print("\n[bold bright_green]Font direset[/bold bright_green]")
            else:
                console.print("\n[bold yellow]Tidak ada font[/bold yellow]")
            time.sleep(1.5)
        elif pilih in FONTS:
            nama, url = FONTS[pilih]

            if not ada_command('curl'):
                console.print("\n[bold yellow]Install curl dulu[/bold yellow]")
                pause()
                continue

            TERMUX_DIR.mkdir(exist_ok=True)
            dst = TERMUX_DIR / "font.ttf"
            if dst.exists():
                backup_file(dst)

            with Progress(
                SpinnerColumn(style="bright_cyan"),
                TextColumn("[bold]{task.description}"),
                BarColumn(complete_style="bright_green"),
                TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                console=console,
            ) as progress:
                task = progress.add_task(f"[cyan]Download {nama}...", total=100)
                for i in range(100):
                    time.sleep(0.02)
                    progress.update(task, advance=1)

                ok = jalankan(f'curl -L -s -o "{dst}" "{url}"')

            if ok and dst.exists() and dst.stat().st_size > 1000:
                jalankan("termux-reload-settings")
                console.print()
                console.print(Panel(
                    f"[bold bright_green]Font '{nama}' dipasang[/bold bright_green]\n\n"
                    f"[dim]Developer: {DEVELOPER}[/dim]",
                    border_style="bright_green",
                    box=DOUBLE,
                ))
            else:
                console.print("\n[bold bright_red]Gagal download[/bold bright_red]")
            pause()
        else:
            console.print("\n[bold bright_red]Pilihan tidak valid[/bold bright_red]")
            time.sleep(1)


def info_sistem():
    clear()

    info = {
        "OS": "Android / Termux",
        "Host": platform.node() or "localhost",
        "User": os.environ.get("USER", "user"),
        "Kernel": platform.release(),
        "Arch": platform.machine(),
        "Shell": os.path.basename(os.environ.get("SHELL", "/bin/sh")),
        "Python": platform.python_version(),
        "Uptime": "-",
        "CPU": "-",
        "RAM": "-",
        "Time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    try:
        with open('/proc/uptime') as f:
            up = float(f.read().split()[0])
            h, m = int(up // 3600), int((up % 3600) // 60)
            info["Uptime"] = f"{h}j {m}m"
    except:
        pass

    try:
        with open('/proc/cpuinfo') as f:
            for line in f:
                if 'Hardware' in line or 'model name' in line:
                    info["CPU"] = line.split(':', 1)[1].strip()[:35]
                    break
    except:
        pass

    try:
        with open('/proc/meminfo') as f:
            data = f.read()
        total = avail = 0
        for line in data.split('\n'):
            if 'MemTotal' in line:
                total = int(line.split()[1]) // 1024
            elif 'MemAvailable' in line:
                avail = int(line.split()[1]) // 1024
        if total:
            used = total - avail
            info["RAM"] = f"{used}/{total} MB ({used*100//total}%)"
    except:
        pass

    logo = """[bold cyan]
    ╔═══════════════╗
    ║   ▄▄▄▄▄▄▄▄    ║
    ║  █  >_    █   ║
    ║  █        █   ║
    ║  █ TERMUX █   ║
    ║  █  v3.0  █   ║
    ║   ▀▀▀▀▀▀▀▀    ║
    ╚═══════════════╝[/bold cyan]"""

    table = Table(show_header=False, box=None, padding=(0, 1))
    table.add_column(style="bold bright_yellow", justify="right", width=8)
    table.add_column(style="bright_white")

    for k, v in info.items():
        table.add_row(f"{k}", f"▸ [bright_cyan]{v}[/bright_cyan]")

    layout = Table.grid(padding=(0, 3))
    layout.add_column()
    layout.add_column()
    layout.add_row(logo, table)

    console.print(Panel(
        layout,
        title=f"[bold bright_magenta]INFO SISTEM - {DEVELOPER}[/bold bright_magenta]",
        border_style="bright_magenta",
        box=DOUBLE,
        padding=(1, 2),
    ))

    console.print()
    pause()


def matrix_rain(durasi=5):
    import random
    chars = 'ｱｲｳｴｵｶｷｸｹｺｻｼｽｾｿﾀﾁﾂﾃﾄﾅﾆﾇﾈﾉ0123456789ABCDEF'
    try:
        cols = shutil.get_terminal_size().columns
    except:
        cols = 80

    clear()
    console.print(Panel(
        f"[bold green]MATRIX RAIN - {DEVELOPER}[/bold green]",
        border_style="green",
        box=ROUNDED,
    ))

    end = time.time() + durasi
    while time.time() < end:
        line = ""
        for _ in range(cols):
            ch = random.choice(chars)
            r = random.random()
            if r < 0.03:
                line += f"[bold bright_white]{ch}[/bold bright_white]"
            elif r < 0.15:
                line += f"[bright_green]{ch}[/bright_green]"
            elif r < 0.35:
                line += f"[green]{ch}[/green]"
            else:
                line += f"[dim green]{ch}[/dim green]"
        console.print(line)
        time.sleep(0.06)


def jam_digital(durasi=8):
    pola = {
        '0': ['███','█ █','█ █','█ █','███'], '1': [' █ ','██ ',' █ ',' █ ','███'],
        '2': ['███','  █','███','█  ','███'], '3': ['███','  █','███','  █','███'],
        '4': ['█ █','█ █','███','  █','  █'], '5': ['███','█  ','███','  █','███'],
        '6': ['███','█  ','███','█ █','███'], '7': ['███','  █','  █','  █','  █'],
        '8': ['███','█ █','███','█ █','███'], '9': ['███','█ █','███','  █','███'],
        ':': ['   ',' █ ','   ',' █ ','   '], ' ': ['   ','   ','   ','   ','   '],
    }
    warna = ["bright_cyan", "bright_green", "bright_yellow", "bright_magenta", "bright_blue", "bright_red"]

    end = time.time() + durasi
    while time.time() < end:
        clear()
        now = datetime.datetime.now()

        baris = [''] * 5
        for i, ch in enumerate(now.strftime('%H:%M:%S')):
            p = pola.get(ch, ['   '] * 5)
            w = warna[i % len(warna)]
            for j in range(5):
                baris[j] += f"[{w}]{p[j]}[/{w}]  "

        content = "\n".join(baris)
        content += f"\n\n[bold white]{now.strftime('%A, %d %B %Y')}[/bold white]"

        console.print(Panel(
            Align.center(content),
            title=f"[bold bright_yellow]JAM - {DEVELOPER}[/bold bright_yellow]",
            border_style="bright_yellow",
            box=DOUBLE,
            padding=(1, 4),
        ))
        time.sleep(0.5)


def status_install():
    clear()
    banner()

    checks = [
        ("ZSH", ada_command('zsh')),
        ("Oh My Zsh", (HOME / ".oh-my-zsh").exists()),
        ("Powerlevel10k", (HOME / ".oh-my-zsh/custom/themes/powerlevel10k").exists()),
        ("zsh-autosuggestions", (HOME / ".oh-my-zsh/custom/plugins/zsh-autosuggestions").exists()),
        ("zsh-syntax-highlighting", (HOME / ".oh-my-zsh/custom/plugins/zsh-syntax-highlighting").exists()),
        ("zsh-completions", (HOME / ".oh-my-zsh/custom/plugins/zsh-completions").exists()),
        ("eza", ada_command('eza')),
        ("bat", ada_command('bat')),
        ("fzf", ada_command('fzf')),
        ("zoxide", ada_command('zoxide')),
        ("Tema Warna", (TERMUX_DIR / "colors.properties").exists()),
        ("Font Custom", (TERMUX_DIR / "font.ttf").exists()),
        (".zshrc", (HOME / ".zshrc").exists()),
    ]

    table = Table(
        title=f"[bold bright_magenta]STATUS INSTALASI - {DEVELOPER}[/bold bright_magenta]",
        box=HEAVY,
        border_style="bright_magenta",
        header_style="bold bright_cyan",
    )
    table.add_column("Status", justify="center", width=8)
    table.add_column("Komponen", style="bold white", width=30)

    for nama, ok in checks:
        if ok:
            table.add_row("[bold bright_green]✓ OK[/bold bright_green]", f"[bright_white]{nama}[/bright_white]")
        else:
            table.add_row("[bold bright_red]✗ NO[/bold bright_red]", f"[dim]{nama}[/dim]")

    console.print(table)

    total = len(checks)
    ok_count = sum(1 for _, ok in checks if ok)
    pct = ok_count * 100 // total

    warna = "bright_green" if pct > 80 else ("bright_yellow" if pct > 50 else "bright_red")
    bar_w = 40
    isi = bar_w * pct // 100
    bar = f"[{warna}]{'█' * isi}[/{warna}][dim]{'░' * (bar_w - isi)}[/dim]"

    console.print()
    console.print(Panel(
        f"{bar}  [bold {warna}]{pct}%[/bold {warna}]\n"
        f"[bright_white]{ok_count}/{total} terinstall[/bright_white]",
        border_style=warna,
        box=ROUNDED,
    ))
    pause()


def apply_all():
    clear()
    banner()

    console.print(Panel(
        f"[bold bright_yellow]INSTALL SEMUA[/bold bright_yellow]\n\n"
        f"[bright_green]✓[/bright_green] ZSH + Oh My Zsh + Plugins\n"
        f"[bright_green]✓[/bright_green] Tema warna Tokyo Night\n"
        f"[bright_green]✓[/bright_green] Font JetBrains Mono\n"
        f"[bright_green]✓[/bright_green] Powerlevel10k prompt\n"
        f"[bright_green]✓[/bright_green] Alias & config\n\n"
        f"[dim]Developer: {DEVELOPER}[/dim]",
        border_style="bright_magenta",
        box=DOUBLE,
        padding=(1, 2),
    ))
    console.print()

    if not Confirm.ask("[bold bright_green]Lanjut install?[/bold bright_green]", default=False):
        console.print("\n[yellow]Dibatalkan.[/yellow]")
        pause()
        return

    install_zsh_silent()

    tema = TEMA["3"]
    content = buat_colors(tema[0], tema[1], tema[2], tema[3], tema[4], tema[5], tema[6], tema[7], tema[8])
    TERMUX_DIR.mkdir(exist_ok=True)
    with open(TERMUX_DIR / "colors.properties", 'w') as f:
        f.write(content)

    if ada_command('curl'):
        jalankan(f'curl -L -s -o "{TERMUX_DIR}/font.ttf" "{FONTS["1"][1]}"')

    jalankan("termux-reload-settings")

    console.print()
    console.print(Panel(
        f"[bold bright_green]SEMUA SELESAI[/bold bright_green]\n\n"
        f"[yellow]Restart Termux sekarang[/yellow]\n"
        f"[yellow]Saat buka ZSH, pilih opsi[/yellow] [bold white]1[/bold white]\n\n"
        f"[dim]Developer: {DEVELOPER}[/dim]",
        border_style="bright_green",
        box=DOUBLE,
        padding=(1, 3),
    ))
    pause()


def preview_tema():
    clear()
    banner()

    console.print(Panel(
        f"[bold bright_magenta]PREVIEW TEMA - {DEVELOPER}[/bold bright_magenta]",
        border_style="bright_magenta",
        box=DOUBLE,
    ))
    console.print()

    for k, tema in TEMA.items():
        nama, bg, fg, w1, w2, w3, w4, w5, err, warna_rich = tema
        preview = f"[on {bg}][{fg}] {nama:^25} [/{fg}][/on {bg}]"
        console.print(f"  [bold yellow][{k:>2}][/bold yellow]  {preview}")
    console.print()
    pause()


def reset_semua():
    clear()
    banner()

    console.print(Panel(
        f"[bold bright_red]RESET SEMUA[/bold bright_red]\n\n"
        f"Backup: [bright_cyan]{BACKUP_DIR}[/bright_cyan]\n"
        f"[dim]Developer: {DEVELOPER}[/dim]",
        border_style="bright_red",
        box=DOUBLE,
    ))
    console.print()

    if not Confirm.ask("[bold bright_red]Yakin reset?[/bold bright_red]", default=False):
        console.print("\n[yellow]Dibatalkan.[/yellow]")
        pause()
        return

    items = [
        (TERMUX_DIR / "colors.properties", "Tema warna"),
        (TERMUX_DIR / "font.ttf", "Font"),
        (HOME / ".zshrc", ".zshrc"),
        (HOME / ".p10k.zsh", ".p10k.zsh"),
    ]

    table = Table(show_header=False, box=ROUNDED, border_style="bright_red")
    table.add_column("Status", justify="center")
    table.add_column("Item")

    for path, nama in items:
        if path.exists():
            backup_file(path)
            path.unlink()
            table.add_row("[bright_green]✓[/bright_green]", f"[white]{nama}[/white]")
        else:
            table.add_row("[dim]-[/dim]", f"[dim]{nama}[/dim]")

    console.print(table)

    bash = shutil.which('bash')
    if bash:
        jalankan(f"chsh -s {bash}")

    jalankan("termux-reload-settings")

    console.print()
    console.print(Panel(
        f"[bold bright_green]Reset selesai[/bold bright_green]\n\n"
        f"[dim]Developer: {DEVELOPER}[/dim]",
        border_style="bright_green",
        box=DOUBLE,
    ))
    pause()


def welcome():
    user = os.environ.get("USER", "user")
    now = datetime.datetime.now()

    banner_art = f"""[bold cyan]
   ╔══════════════════════════════════════════════╗
   ║  [bold magenta]✦  M Y T E R M U X  ✦[/bold magenta][bold cyan]                     ║
   ║  [bold yellow]Halo [/bold yellow][bold white]{user}[/bold white][bold yellow]![/bold yellow][bold cyan]                              ║
   ║  [bold bright_magenta]Developer: {DEVELOPER}[/bold bright_magenta][bold cyan]           ║
   ╚══════════════════════════════════════════════╝[/bold cyan]"""

    console.print(banner_art)
    console.print()
    console.print(f"  [bold bright_green]➜[/bold bright_green] [bold white]Tanggal :[/bold white] {now.strftime('%A, %d %B %Y')}")
    console.print(f"  [bold bright_green]➜[/bold bright_green] [bold white]Waktu   :[/bold white] {now.strftime('%H:%M:%S')}")
    console.print(f"  [bold bright_green]➜[/bold bright_green] [bold white]Shell   :[/bold white] zsh + oh-my-zsh")
    console.print()


def menu():
    clear()
    banner()

    checks = [
        ada_command('zsh'),
        (HOME / ".oh-my-zsh").exists(),
        (TERMUX_DIR / "colors.properties").exists(),
        (TERMUX_DIR / "font.ttf").exists(),
    ]
    pct = sum(checks) * 100 // len(checks)
    warna = "bright_green" if pct >= 75 else ("bright_yellow" if pct >= 50 else "bright_red")
    status_text = f"[{warna}]●[/{warna}] [bold white]Status:[/bold white] [bold {warna}]{pct}%[/bold {warna}]"

    menu_table = Table(
        title=f"[bold bright_magenta]MENU UTAMA[/bold bright_magenta]  {status_text}",
        box=HEAVY,
        border_style="bright_magenta",
        header_style="bold bright_cyan",
        padding=(0, 1),
    )
    menu_table.add_column("No", style="bold yellow", justify="center", width=5)
    menu_table.add_column("Menu", style="bold white", width=35)
    menu_table.add_column("Kategori", style="dim cyan", width=18)

    items = [
        ("1", "Install Semua (All-in-One)", "INSTALASI"),
        ("2", "Install ZSH + Oh My Zsh", "INSTALASI"),
        ("3", "Ganti Warna Termux", "TAMPILAN"),
        ("4", "Ganti Font", "TAMPILAN"),
        ("5", "Preview Semua Tema", "TAMPILAN"),
        ("6", "Info Sistem", "INFO"),
        ("7", "Status Instalasi", "INFO"),
        ("8", "Matrix Rain Effect", "EFEK"),
        ("9", "Jam Digital", "EFEK"),
        ("10", "Reset Semua", "LAIN-LAIN"),
        ("0", "Keluar", "LAIN-LAIN"),
    ]

    for no, nama, kat in items:
        warna_no = "bright_red" if no == "0" else "bright_yellow"
        warna_nama = "dim red" if no == "0" else "white"
        menu_table.add_row(
            f"[bold {warna_no}][{no}][/bold {warna_no}]",
            f"[{warna_nama}]{nama}[/{warna_nama}]",
            f"[{kat}]",
        )

    console.print(menu_table)
    console.print()

    console.print(Panel(
        f"[bold bright_magenta]Developer: {DEVELOPER}[/bold bright_magenta]",
        border_style="dim magenta",
        box=ROUNDED,
    ))


def arg_handler():
    if len(sys.argv) < 2:
        return False
    arg = sys.argv[1]
    if arg == "--welcome":
        welcome()
        return True
    if arg == "--color":
        ganti_warna()
        return True
    if arg == "--font":
        ganti_font()
        return True
    if arg == "--info":
        info_sistem()
        return True
    return False


def main():
    if arg_handler():
        return

    clear()
    banner()

    with Progress(
        SpinnerColumn(style="bright_cyan"),
        TextColumn("[bold bright_white]{task.description}"),
        BarColumn(complete_style="bright_magenta"),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        console=console,
    ) as progress:
        task = progress.add_task(f"[cyan]Memuat MyTermux by {DEVELOPER}...", total=100)
        for _ in range(100):
            time.sleep(0.008)
            progress.update(task, advance=1)

    while True:
        menu()
        try:
            pilih = Prompt.ask("[bold bright_green]➜ Pilih menu[/bold bright_green]", default="0").strip()
        except (KeyboardInterrupt, EOFError):
            console.print("\n\n[bold yellow]Sampai jumpa[/bold yellow]\n")
            break

        actions = {
            '1': apply_all,
            '2': install_zsh,
            '3': ganti_warna,
            '4': ganti_font,
            '5': preview_tema,
            '6': info_sistem,
            '7': status_install,
            '8': lambda: (matrix_rain(5), pause()),
            '9': lambda: (jam_digital(8), pause()),
            '10': reset_semua,
        }

        if pilih == '0':
            clear()
            console.print()
            console.print(Panel(
                f"[bold bright_green]Terima kasih sudah pakai MyTermux[/bold bright_green]\n\n"
                f"[bold bright_magenta]Developer: {DEVELOPER}[/bold bright_magenta]\n\n"
                f"[dim]Sampai jumpa[/dim]",
                border_style="bright_green",
                box=DOUBLE,
                padding=(1, 3),
            ))
            console.print()
            break
        elif pilih in actions:
            actions[pilih]()
        else:
            console.print("\n[bold bright_red]Pilihan tidak valid[/bold bright_red]")
            time.sleep(1)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n\n[bold yellow]Dibatalkan[/bold yellow]\n")
    except Exception as e:
        console.print(f"\n[bold red]Error: {e}[/bold red]\n")
        import traceback
        traceback.print_exc()