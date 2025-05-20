from googledrivedownloader import download_file_from_google_drive

#https://drive.google.com/file/d/1XRKn8r9Bcf_PB6rIq9eq84-5VPTtWlzG/view?usp=sharing

download_file_from_google_drive(file_id='1XRKn8r9Bcf_PB6rIq9eq84-5VPTtWlzG',
                                    dest_path='/home/ubuntu/curve/tensorflow_datasets/ck_counter_dataset.tar',
                                    showsize=True,
                                    unzip=True)