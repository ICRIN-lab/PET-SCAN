import nibabel
import os


def pet_intensity_normalisation(path_pet, path_ref_region, path_pet_suvr):
    import os
    import nibabel as nib
    import numpy as np

    #
    # Intensity normalisation of a PET image using average uptake in a reference region
    # path_pet: path to the input PET image in nifti
    # path_ref_region: path to the reference region mask in nifti
    # path_pet_suvr: path to the output intensity normalised PET image in nifti
    #

    # Load PET image
    pet_nifti = nib.load(path_pet)
    pet_img = pet_nifti.get_data()

    # Load mask of the reference region and set all the background voxels to NaN
    mask_nifti = nib.load(path_ref_region)
    mask_img = mask_nifti.get_data() + 0.0
    mask_img[mask_img == 0] = np.nan

    # Compute average PET uptake within the reference region
    average_pet_in_mask = np.nanmean(np.multiply(pet_img, mask_img))

    # Generate SUVR image by dividing each voxel of the PET image
    # by the average PET uptake within the reference region
    pet_suvr_img = np.divide(pet_img, average_pet_in_mask)

    # Save PET SUVR image as nifti
    pet_suvr_nifti = nib.Nifti1Image(pet_suvr_img, pet_nifti.affine, pet_nifti.header)
    nib.save(pet_suvr_nifti, path_pet_suvr)


# path_pet = 'sub-CAPP01P001MC_ses-M00_task-rest_acq-FDG_vsize-1.5_smooth-2.15_pet.nii.gz'
# path_ref_region = 'sub-CAPP01P001MC_Pons.nii.gz'
# path_pet_suvr = 'sub-CAPP01P001MC_ses-M00_task-rest_acq-FDG_vsize-1.5_smooth-2.15_suvr-pons_pet_test.nii.gz'

# pet_intensity_normalisation(path_pet,path_ref_region,path_pet_suvr)


path_ref_region = '/home/icrin_3/Documents/PET-Scan/preproc_PET_2021/WFU_PickAtlas_3.0.5b_MNI_atlas_TD_lobe_pons_eroded-4mm.nii'

wd = '/home/icrin_3/Documents/PET-Scan/BIDS_nifti_dataset/Rennes/'
cpt = 0
L = ["OCD", "OCD-DBS", "HC", "OCD-rTMS"]
for path, dirs, files in os.walk(wd):
    for subject_identifier in dirs:
        if subject_identifier in L:
            continue
        pet_file = os.path.join(path, subject_identifier,
                                subject_identifier + '_ses-00_task-rest_acq-fdg_rec-ac_pet_space-mni.nii.gz')
        pet_suvr_file = os.path.join(path, subject_identifier,
                                     subject_identifier + '_ses-00_task-rest_acq-fdg_rec-ac_pet_space-mni_suvr-pons_1'
                                                          '.nii.gz')

        pet_intensity_normalisation(os.path.join(path, pet_file), path_ref_region, os.path.join(path, pet_suvr_file))
