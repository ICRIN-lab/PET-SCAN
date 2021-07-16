#!/bin/bash

input_data="/home/icrin_3/Documents/PET-Scan/BIDS_nifti_dataset/Rennes/"
list_of_subjects=$(ls ${input_data}*/*/Sub*_task-rest_acq-fdg_rec-ac_pet.nii*)

which flirt
for subject in ${list_of_subjects[*]}
do
    fname=$(basename ${subject})
    input_subject=${fname%".nii"}
    folder=$(dirname ${subject})

    echo "###   ${input_subject}"
    flirt -in ${subject} -ref /home/icrin_3/Documents/spm12/toolbox/OldNorm/PET.nii -omat ${folder}/${input_subject}_space-mni.txt -out ${folder}/${input_subject}_space-mni.nii.gz
done
