#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transform the members.yml file to an Excel file and folder for the google drive

This script reads the yaml configuration files and converts them to Excel, and
it extracts the images and moves them to a folder in the output directory

Usage::

    ./scripts/members_to_xls.py output_file.xlsx

Created on Fri May 29

@author: Philipp S. Sommer
"""
import pandas as pd
import yaml
import argparse
import shutil
import os
import os.path as osp

parser = argparse.ArgumentParser()

parser.add_argument("output_file", metavar="output_file.xlsx",
                    help=("The Excel file to write to. We will also generate"
                          "a folder with the same name that contains the "
                          "avatars."))


def maybe_copy_image(path):
    if path.startswith('/assets/images/'):
        os.makedirs(img_local, exist_ok=True)
        fname = osp.basename(path)
        shutil.copyfile(osp.join(img_web, fname),
                         osp.join(img_local, fname))
        return path.replace('/assets/images/', '')
    return path


args = parser.parse_args()

yml_dir = osp.join('_data', 'committee')
yml_file = osp.join(yml_dir, 'members.yml')
xls_file = args.output_file
img_web = osp.join('assets', 'images')
img_local = osp.splitext(args.output_file)[0]

teams = ['national_chapters', 'committees', 'programme_teams']

with open(yml_file) as f:
    entries = yaml.load(f, yaml.SafeLoader)

df = pd.DataFrame.from_dict(entries)

avatars = df.avatar.copy()

df['avatar'] = df.avatar.apply(maybe_copy_image)
df['teams'] = df['teams'].apply(', '.join)

os.makedirs(osp.dirname(xls_file) or '.', exist_ok=True)

writer = pd.ExcelWriter(xls_file)

df.to_excel(writer, sheet_name='members', index=False)

for team in teams:
    team_file = osp.join(yml_dir, team + '.yml')
    with open(team_file) as f:
        config = yaml.load(f, yaml.SafeLoader)
    team_df = pd.DataFrame.from_dict(config, orient='index').fillna('')
    team_df.to_excel(writer, sheet_name=team)

writer.save()

