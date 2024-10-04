# BinCrack: A Lightweight Binary Disassembler

BinCrack is a modular and lightweight binary disassembler, designed for analyzing and reversing binary files, with a focus on malware analysis. It translates machine code into human-readable assembly instructions, providing insights into the internal structure of executables in various formats such as PE and ELF.

## Features

- **Supports Multiple Formats**: Initial support for PE (Portable Executable) and ELF (Executable and Linkable Format).
- **Extensible Architecture**: Easily expandable to include more architectures like ARM, MIPS, etc.
- **Control Flow Analysis**: Understand the flow of execution within the binary.
- **Data Flow Analysis**: Analyze how data moves through the code.
- **Flexible Integration**: Can be integrated into larger malware analysis pipelines or used as a standalone tool.
- **Open Source**: Community-driven development and contributions are welcome.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Required dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/BinCrack.git
    ```

2. Navigate into the project directory:
    ```bash
    cd BinCrack
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage

To disassemble a binary file:
```bash
python -m bincrack disassemble <path_to_binary_file>
