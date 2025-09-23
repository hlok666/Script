#!/usr/bin/env python3
"""
Haplotype Data Organizer Script

This script reads data_analysis.json and organizes the data by haplotype (Hap0-Hap4).
It extracts specific fields (x, y, a, data_1) for each haplotype group and saves
the restructured data to a new JSON file.
"""

import json
import os
from typing import Dict, List, Any
from collections import defaultdict


def read_data_analysis_file(file_path: str) -> Dict[str, Any]:
    """
    Read the data_analysis.json file.
    
    Args:
        file_path: Path to the data_analysis.json file
        
    Returns:
        Parsed JSON data
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        json.JSONDecodeError: If the file contains invalid JSON
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def organize_data_by_haplotype(data: Dict[str, Any]) -> Dict[str, Dict[str, Any]]:
    """
    Organize data by haplotype groups (Hap0-Hap4).
    
    Args:
        data: Raw data from data_analysis.json
        
    Returns:
        Dictionary organized by haplotype with aggregated fields
    """
    # Initialize result structure for all haplotypes
    haplotype_data = {
        "Hap0": {"x": [], "y": [], "a": [], "data_1": {}},
        "Hap1": {"x": [], "y": [], "a": [], "data_1": {}},
        "Hap2": {"x": [], "y": [], "a": [], "data_1": {}},
        "Hap3": {"x": [], "y": [], "a": [], "data_1": {}},
        "Hap4": {"x": [], "y": [], "a": [], "data_1": {}},
    }
    
    # Get the data list from the input
    data_list = data.get('data', [])
    
    # Group data by haplotype
    for item in data_list:
        hap = item.get('hap')
        if hap in haplotype_data:
            # Extend lists for x, y, a fields
            if 'x' in item:
                haplotype_data[hap]['x'].extend(item['x'])
            if 'y' in item:
                haplotype_data[hap]['y'].extend(item['y'])
            if 'a' in item:
                haplotype_data[hap]['a'].extend(item['a'])
            
            # Merge data_1 dictionaries
            if 'data_1' in item:
                if not haplotype_data[hap]['data_1']:
                    haplotype_data[hap]['data_1'] = item['data_1'].copy()
                else:
                    # If multiple data_1 objects exist for the same haplotype,
                    # we'll merge them (this is a simple merge strategy)
                    haplotype_data[hap]['data_1'].update(item['data_1'])
    
    return haplotype_data


def save_organized_data(organized_data: Dict[str, Dict[str, Any]], output_path: str) -> None:
    """
    Save the organized data to a JSON file.
    
    Args:
        organized_data: Data organized by haplotype
        output_path: Path where to save the output file
    """
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(organized_data, file, indent=2, ensure_ascii=False)


def main():
    """
    Main function to process the haplotype data.
    """
    # Define file paths
    input_file = 'data_analysis.json'
    output_file = 'organized_haplotype_data.json'
    
    try:
        # Read the input data
        print(f"Reading data from {input_file}...")
        raw_data = read_data_analysis_file(input_file)
        
        # Organize data by haplotype
        print("Organizing data by haplotype...")
        organized_data = organize_data_by_haplotype(raw_data)
        
        # Save the organized data
        print(f"Saving organized data to {output_file}...")
        save_organized_data(organized_data, output_file)
        
        # Output the file path for verification
        output_path = os.path.abspath(output_file)
        print(f"✅ Successfully organized haplotype data!")
        print(f"📁 Output file saved at: {output_path}")
        
        # Display summary
        print("\n📊 Summary:")
        for hap, data in organized_data.items():
            x_count = len(data['x'])
            y_count = len(data['y'])
            a_count = len(data['a'])
            data_1_keys = len(data['data_1'])
            print(f"  {hap}: x({x_count}), y({y_count}), a({a_count}), data_1({data_1_keys} keys)")
        
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("Please ensure data_analysis.json exists in the current directory.")
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        print("Please check that data_analysis.json contains valid JSON.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()