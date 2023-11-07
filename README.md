[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/qMYffwgb)

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12037553&assignment_repo_type=AssignmentRepo)
# RETRO SNAKE

Este é um projeto de um jogo desenvolvido por Ana Beatriz da Cunha e Artur Rizzi na disciplina Developer Life do semestre do curso de Ciência da Computação do Insper. O jogo foi desenvolvido em Python, utilizando o módulo [curses](https://docs.python.org/3/library/curses.html) para a interface gráfica e as sprites foi desenvolvido pela aluna Ana Beatriz da Cunha no site [curses](https://www.piskelapp.com).

## Descrição do jogo

O Retro Snake consiste em um jogo clássico da cobrinha que come as maçãs para ficar maior mas nesse além disso a cobra enfrenta o vilão representado pelo coelho.

## Como jogar

Para jogar, é necessário ter o Python 3.10 instalado na máquina. Além disso, se você estiver no Windows, consulte o [guia abaixo](#jogando-no-windows) para mais informações.

Após instalar a biblioteca, clone este repositório e execute o arquivo `jogo.py`, dentro da pasta `codigo`. O jogo será aberto em uma janela de terminal e pode ser jogado com as seguintes teclas:

- **Movimento**: teclas de seta ou teclas W,S,D,A
- **Fechar jogo**: tecla "esc"

### Jogando no Windows

No Windows é necessário instalar algumas dependências adicionais. O módulo utilizado por este projeto pode não funcionar corretamente com o prompt de comando padrão do Windows. Por esse motivo, comece instalando o Windows Terminal. Para isso, siga [estes passos de instalação](https://learn.microsoft.com/pt-br/windows/terminal/install).

Com o Windows Terminal instalado, precisamos instalar também o módulo `windows-curses`, utilizando o gerenciador de pacotes pip. Para isso, abra o terminal e execute o seguinte comando:

```bash
pip install windows-curses
```

Pronto! Agora você pode se divertir com o Retro Snake!.
