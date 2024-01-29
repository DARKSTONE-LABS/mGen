# mGen - NFT Metadata Generator

## Overview
mGen is an intuitive application designed to create metadata files for NFT (Non-Fungible Token) collections. It simplifies the process of generating metadata for NFTs, particularly for collections on the Solana blockchain, by allowing users to define various traits and attributes.

## Features
- **Intuitive GUI**: Built with Tkinter, mGen offers a user-friendly graphical interface for easy navigation and usage.
- **Customizable Trait Types**: Users can add and define multiple trait types for their NFT collection.
- **Automatic JSON Metadata Generation**: Generates Solana-compatible metadata files in JSON format for the specified quantity of NFTs.
- **Efficient File Handling**: Organizes generated metadata files into a designated folder for ease of access and management.

## Installation
Ensure you have Python (preferably version 3.11 or later) installed on your system to run mGen.

To use mGen, clone the repository:
```bash
git clone https://github.com/DARKSTONE-LABS/mGen.git
cd mGen
```

## Usage
1. **Launch the Application**:
   Execute `python mGen.py` to open the application.

2. **Input Collection Details**:
   - Fill in the name and description for your NFT collection.
   - Specify the number of NFTs to generate metadata for.

3. **Define Traits**:
   - Use the '+ Add Another Trait Type' button to add new traits.
   - For each trait, enter its name and choose a file with the trait's possible values.

4. **Generate Metadata**:
   - Click on 'Generate Metadata' after setting up all traits.
   - The application creates a `generated_metadata` folder where it saves the JSON files, starting from `0.json`.

## Contributing
Your contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

## License
This project is distributed under the MIT License. See the `LICENSE` file in the repository for more details.

