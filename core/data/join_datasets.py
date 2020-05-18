import sys
import os
import warnings
import argparse
import json
import pandas as pd
import time

def parse_args():
    """Parse arguments."""
    # Parameters settings
    parser = argparse.ArgumentParser(description="Join events")

    # Dataset setting
    parser.add_argument('--config', type=str, default="config.json", help='Configuration file')

    # parse the arguments
    args = parser.parse_args()

    return args


def main():

    args = parse_args()       

    # load configurations of datasets
    configs = json.load(open(args.config, 'r'))

    # Get values fron config file
    datasets_dir = configs['join']['datasets_dir']
    output_path = configs['join']['output_path']
    output_filename = configs['join']['output_filename']
    n_split = configs['join']['n_split']

    # Get the list of dataset in the input dir 
    event_files = pd.DataFrame(os.listdir(datasets_dir))

    # Initializing the final dataset
    tracks_final = pd.DataFrame()
    tracks_events = pd.DataFrame()

    # lists
    list_events = []

    # Joining the datasets (concatenate)
    for index, row in event_files.iterrows():
        path = datasets_dir + '/' + str(row[0])
        print(str(row[0]))
        tracks = pd.read_csv(path)
        tracks_final = pd.concat([tracks_final, tracks], ignore_index=True)
        
        list_events_local = []
        event_name = str(row[0])
        event_id = event_name[5:]
        n_tracks_in_event = tracks.shape[0]
        list_events_local = [event_id] * n_tracks_in_event
        list_events.extend(list_events_local)
    
    tracks_events['event_id'] = list_events

    # get time
    timestr = '_' + time.strftime("%Y%m%d%H%M%S")

    # splitting the final dataset
    if type(n_split) is int:
        if n_split >  tracks_final.shape[0]:
            n_split = tracks_final.shape[0]
            wrn_msg = ('The number of tracks to split is greater than the number of tracks in '
                       'the file.\nn_plit will be: ' +  str(n_split) +
                       ' (the number of tracks in the file)')
            warnings.warn(wrn_msg, RuntimeWarning, stacklevel=2)

        df_split = tracks_final.iloc[:n_split,:]
        df_split_events = tracks_events.iloc[:n_split,:]
        df_split.to_csv(output_path + '/' + output_filename[:-4] + timestr +  '_tracks' + output_filename[-4:], index = False)
        df_split_events.to_csv(output_path + '/' + output_filename[:-4] + timestr + '_events' + output_filename[-4:], index = False)
    else:
        tracks_final.to_csv(output_path + '/' + output_filename[:-4] + timestr + '_tracks' + output_filename[-4:], index = False)
        tracks_events.to_csv(output_path + '/' + output_filename[:-4] + timestr + '_events' + output_filename[-4:] , index = False)

if __name__=='__main__':
    main()
