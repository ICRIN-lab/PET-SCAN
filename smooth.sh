input_data="/home/redwan.maatoug/Documents/BIDS_nifti_dataset/Rennes/OCD/"
list_of_subjects=$(ls ${input_data}*/*.nii*)

which fslmaths
for subject in ${list_of_subjects[*]}
do
    fname=$(basename ${subject})
    input_subject=${fname%".nii"}
    folder=$(dirname ${subject})

    echo "###   ${input_subject}"
    fslmaths ${subject} ${folder}/${input_subject}.nii.gz
done
