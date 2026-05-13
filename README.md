# 7 Maravilhas do Mundo Moderno — Quick Sort Interativo

Uma aplicação desktop educativa que combina um jogo de ordenação cronológica com uma visualização animada do algoritmo **Quick Sort**, usando as 7 Maravilhas do Mundo Moderno como tema.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green) ![Pillow](https://img.shields.io/badge/Imagens-Pillow-orange)

---

## Sobre o projeto

O usuário vê 7 cards com fotos das maravilhas do mundo e deve arrastá-los para ordenar do **mais antigo ao mais recente**. Após verificar a resposta, é possível assistir ao Quick Sort executar a ordenação correta em tempo real, com animações que mostram cada etapa do algoritmo — pivô, partição e reagrupamento.

---

## Funcionalidades

- **Drag & drop** — arraste os cards para reposicioná-los
- **Verificação** — confere se a ordem cronológica está correta e revela os anos
- **Animação do Quick Sort** — visualização passo a passo com cores distintas para pivô, grupo menor e grupo maior
- **Embaralhar** — reinicia o jogo com uma nova ordem aleatória
- **Banner de status** — mensagens contextuais em cada etapa do algoritmo

---

## Maravilhas incluídas

| Monumento | Ano |
|---|---|
| Muralha da China | ~700 a.C. |
| Petra | 312 a.C. |
| Coliseu | 80 d.C. |
| Chichen Itza | ~600 d.C. |
| Machu Picchu | ~1450 |
| Taj Mahal | 1653 |
| Cristo Redentor | 1931 |

---

## Pré-requisitos

- Python 3.8 ou superior
- [Pillow](https://pillow.readthedocs.io/)

```bash
pip install Pillow
```

> Tkinter já vem incluído na instalação padrão do Python. Se não estiver disponível, instale com `sudo apt install python3-tk` (Linux).

---

## Estrutura de arquivos

```
projeto/
├── main.py
└── imagens/
    ├── cristo.jpg
    ├── coliseu.jpg
    ├── petra.jpg
    ├── machu.jpg
    ├── tajmahal.jpg
    ├── chichen.jpg
    └── muralha.jpg
```

As imagens devem ter pelo menos **100×72 px** e ser colocadas na pasta `imagens/` no mesmo diretório que `main.py`.

---

## Como executar

```bash
python main.py
```

---

## Como jogar

1. **Arraste** os cards para ordenar as maravilhas da mais antiga para a mais recente
2. Clique em **✓ Verificar minha ordem** para checar sua resposta
   - ✅ Acertou? Parabéns! Os anos são revelados
   - ❌ Errou? Clique em **▶ Ver o Quick Sort organizar** para assistir ao algoritmo em ação
3. Clique em **↺ Embaralhar novamente** para jogar de novo

---

## Visualização do Quick Sort

Durante a animação, cada etapa é destacada com cores diferentes:

| Cor | Significado |
|---|---|
| 🟡 Amarelo | Pivô atual |
| 🟠 Laranja | Elementos menores que o pivô |
| 🔵 Azul | Elementos maiores que o pivô |
| 🟣 Roxo | Elemento fixado na posição correta |

---

## Tecnologias

- **Tkinter** — interface gráfica e canvas
- **Pillow (PIL)** — carregamento e redimensionamento das imagens
- **Python puro** — lógica do Quick Sort e sistema de animação por frames
