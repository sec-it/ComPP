#!/usr/bin/env python3
# coding: utf-8

__author__ = "Alex Garrido"
__copyright__ = "Copyright 2021, SEC-IT"
__version__ = "1.0.0"
__maintainer__ = "Alex GARRIDO"

"""Company Passwords Profiler (ComPP)"""

import argparse
import itertools
import json
import os
import sys
from colorama import init, Fore, Back, Style

def print_header():
    c = """
 ▄████████  ▄██████▄    ▄▄▄▄███▄▄▄▄      ▄███████▄    ▄███████▄ 
███     ██ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
███    █▀  ██     ███ ███   ███   ██    ███    ███    ██    ███ 
███        ███    ███ ███   ███   ███   ███    ███   ███    ███ 
███        ███     ██ ███   ███   ███ ▀█████████▀  ▀█████████▀  
██     █▄  ███    ███ ███   ███   ███   ███          ███        
███    ███ ███    ███ ███    ██   ███   ██           ██         
 ███████▀   ▀██████▀   ▀█   ███   █▀   ▄████▀       ▄████▀  :)    
"""
    print(Fore.GREEN + c)

def add_passwords(pwds):
    """Add passwords to wordlist"""
    if args.output:
        with open(args.output, "a+") as f:
            for p in pwds:
                f.write(p+'\r\n')
    else:
        print('\r\n'.join(pwds))

def bake(fields):
    """Compute passwords derivation."""

    # Add fields with case modifications
    lower_case = [f.lower() for f in fields]
    upper_case = [f.upper() for f in fields]
    capit_case = [f.capitalize() for f in fields]

    mixed_case_fields = []
    mixed_case_fields += fields
    mixed_case_fields += lower_case
    mixed_case_fields += upper_case
    mixed_case_fields += capit_case

    mixed_case_fields = list(set(mixed_case_fields))  # Remove duplicat from final list
    final_fields = list(mixed_case_fields)
    
    # Add fields combinations (itertools permutations x2, x3 ...)
    # Note: we do not use final_fields to avoid having the same word twice or more
    if args.permutations >= 2:
        for n in range(2, args.permutations+1):
            fields_pn = [''.join(list(x)) for x in list(itertools.permutations(fields, n))]
            lower_case_pn = [''.join(list(x)) for x in list(itertools.permutations(lower_case, n))]
            upper_case_pn = [''.join(list(x)) for x in list(itertools.permutations(upper_case, n))]
            capit_case_pn = [''.join(list(x)) for x in list(itertools.permutations(capit_case, n))]
            final_fields += fields_pn
            final_fields += lower_case_pn
            final_fields += upper_case_pn
            final_fields += capit_case_pn

    final_fields = list(set(final_fields))  # Remove duplicat from final list
        
    # Add years at the end of generated passwords

    ffields_year = []
    for f in final_fields:
        for i in range(config["years"]["start"],config["years"]["stop"]+1):
            ffields_year.append(f"{f}{i}")
    final_fields += ffields_year

    # Add special chars at the end of generated passwords
    
    ffields_special = []
    for f in final_fields:
        for c in config["symbols"]:
            ffields_special.append(f"{f}{c}")
    final_fields += ffields_special

    # Only for original fields, compute permutations with special char between 2 words
    if args.permutations >= 2:
        fields_separated = []  
        for x in list(itertools.permutations(fields, 2)):  # Company@App, App!75000, ...
            for c in config["symbols"]:
                fields_separated.append(x[0]+c+x[1])
        final_fields += fields_separated

    # Add numbers
    if args.numbers:
        ffields_number = []
        for f in final_fields:
            for n in range(100):
                ffields_number.append(f"{f}{n}")
            for n in ["000000", "000", 111, 123, 1234, 
                12345, 111111, 123123, 123321, 123456, 
                1234567, 12456789, 124567890]:  # Common numbers
                ffields_number.append(f"{f}{n}")
        final_fields += ffields_number

    # Add l337 5p34k
    if args.leet:
        ffields_leet = []
        for f in final_fields:
            w = ""
            for l in f:
                if l.lower() in config["leet"]:
                    w += config["leet"][l.lower()]
                else:
                    w += l
            if w != f:
                ffields_leet.append(w)
        final_fields += ffields_leet

    # Apply config.json size restrictions filter

    final_fields_correct_size = []
    for f in final_fields:
        if config["size"]["min"] <= len(f) <= config["size"]["max"]:
            final_fields_correct_size.append(f)

    final_fields_correct_size = list(set(final_fields_correct_size))
    final_fields_correct_size.sort()
    add_passwords(final_fields_correct_size)

def clear_list(string_list):
    """Transform a comma separated list (str) into a python list."""
    return [x.strip() for x in string_list.split(',')]

def generate():
    """Generate wordlist with user inputs."""

    if args.input_file:
        with open(args.input_file) as json_file:
            data = json.load(json_file)
        company_names = data["company"]
        zip_codes = data["zip_codes"]
        cities = data["cities"]
        keywords = data["keywords"]

    else:  # If no file is provided, ask user input
        init(autoreset=True)
        print(Fore.GREEN + "Fill the differents inputs (case insensitive). Leave blank for unknow fields.\n")
        plus = Fore.RED + "[+] " + Style.RESET_ALL
        company_names = input(plus + "Enter company/application names (comma separated): ")
        company_names = clear_list(company_names)
        
        zip_codes = input(plus + "Enter company zip codes (comma separated): ")
        zip_codes = clear_list(zip_codes)
        
        cities = input(plus + "Enter company cities names (comma separated): ")
        cities = clear_list(cities)

        keywords = input(plus + "Useful keywords (comma separated): ")
        keywords = clear_list(keywords)

    fields = list(set(company_names + zip_codes + cities + keywords))
    bake(fields)

def get_parser():
    """Parse arguments for main."""
    parser = argparse.ArgumentParser(
        description="Company Passwords Profiler (ComPP)"
    )
    
    parser.add_argument('input_file', nargs='?', help="company.json input file",  default=None)

    parser.add_argument('-p', '--permutations', type=int, default=2, help='Number of permutations')

    parser.add_argument('-c', '--config', type=argparse.FileType('r'), help='Configuration file')

    parser.add_argument("-l", "--leet", action="store_true",
                           help="Add 1337 passwords transformation")

    parser.add_argument("-n", "--numbers", action="store_true",
                        help="Add numbers to password")

    parser.add_argument("-o", "--output", 
                        help="Directs the output to a file of your choice")

    parser.add_argument("-v", "--version", action="store_true", 
                       help="Show the version of this program")

    return parser

def main():
    global args, config

    if sys.version_info < (3, 7):
        sys.stdout.write("Sorry, dirsearch requires Python 3.7 or higher\n")
        sys.exit(1)

    print_header()
    parser = get_parser()
    args = parser.parse_args()

    # Load config
    script_path = os.path.dirname(os.path.realpath(__file__))
    if args.config:
        config = json.load(args.config)
    else:
        with open(script_path+"/config.json") as json_file:
            config = json.load(json_file)

    if args.version:
        print(__version__)
    else:
        generate()

if __name__ == "__main__":
    main()