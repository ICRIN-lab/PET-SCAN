input_data="/home/icrin_3/PET-Scan/BIDS_nifti_dataset/Rennes/OCD/"
list_of_subjects=$(ls ${input_data}*/Sub-OCD-Rennes-01_ses-00_task-rest_acq-fdg_rec-ac_pet.nii*)

which flirt
for subject in ${list_of_subjects[*]}
do
    fname=$(basename ${subject})
    input_subject=${fname%".nii"}
    folder=$(dirname ${subject})

    echo "###   ${input_subject}"
    flirt -in ${subject} -ref /home/icrin_3/PET-Scan/preproc_PET_2021/PET.nii -omat ${folder}/${input_subject}_space-mni.txt -out ${folder}/${input_subject}_space-mni_1.nii.gz
done
