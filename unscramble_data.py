#!/usr/bin/env python3

import os
import sys
import csv
import random

def main():

    # read solution from csv file
    solution = {}
    with open("solution.csv", 'r', newline='') as secret_code_data:
        reader=csv.DictReader(secret_code_data)
        for row in reader:
            real = row['true_char']
            illusion = row['false_char']
            solution[illusion] = real

    # unscramble ratings using secret code
    unscrambled_ratings = []
    with open("scrambled_ratings.csv", 'r', newline='') as file:

        reader = csv.DictReader(file)

        for row in reader:
            unscrambled_rating = {
                'name': unscramble(row['name'], solution),
                'item': unscramble(row['item'], solution),
                'rating': row['rating']
            }
            
            # hint: fix me
            unscrambled_ratings.insert(0, unscrambled_rating

    # write unscrambled ratings to csv

    with open ("unscrambled_ratings.csv", 'w', newline='') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=["name", "item", "rating"])
        writer.writeheader()

        for rating in unscrambled_ratings:
            writer.writerow(rating)

def unscramble(input, crypto):
    scrambled_chars = []
    for character in input:
        if character.isalpha():
            scrambled_chars.append(crypto[character])
        else:
            scrambled_chars.append(character)
    return ''.join(scrambled_chars)

if __name__ == '__main__':
    main()