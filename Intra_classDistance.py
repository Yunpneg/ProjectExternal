import matplotlib.pyplot as plt
import numpy as np


# The height of bar is the mean value;
# The black plot is the standard deviation.

def standardError(normal, mutation):
    # Get the average
    normal_mean = np.mean(normal)
    sep1_C_mean = np.mean(mutation[0])
    sep1_V_mean = np.mean(mutation[1])
    sep2_C_mean = np.mean(mutation[2])
    sep2_V_mean = np.mean(mutation[3])
    sep3_C_mean = np.mean(mutation[4])
    sep3_V_mean = np.mean(mutation[5])
    sep4_C_mean = np.mean(mutation[6])
    sep4_V_mean = np.mean(mutation[7])

    # Get the standard deviation
    normal_std = np.std(normal)
    sep1_C_std = np.std(mutation[0])
    sep1_V_std = np.std(mutation[1])
    sep2_C_std = np.std(mutation[2])
    sep2_V_std = np.std(mutation[3])
    sep3_C_std = np.std(mutation[4])
    sep3_V_std = np.std(mutation[5])
    sep4_C_std = np.std(mutation[6])
    sep4_V_std = np.std(mutation[7])

    materials = ['normal', 'sep1-C', 'sep1-V', 'sep2-C', 'sep2-V', 'sep3-C', 'sep3-V', 'sep4-C', 'sep4-V']
    x_pos = np.arange(len(materials))
    ave = [normal_mean, sep1_C_mean, sep1_V_mean, sep2_C_mean, sep2_V_mean, sep3_C_mean,
           sep3_V_mean, sep4_C_mean, sep4_V_mean]
    error = [normal_std, sep1_C_std, sep1_V_std, sep2_C_std, sep2_V_std, sep3_C_std,
             sep3_V_std, sep4_C_std, sep4_V_std]

    # Build the plot
    fig, ax = plt.subplots()
    ax.bar(x_pos, ave, yerr=error, align='center', alpha=0.5, ecolor='black', capsize=10)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(materials)
    ax.yaxis.grid(True)

    # Save the figure and show
    plt.tight_layout()
    plt.savefig('Nine_Type_FLower_error_bars.png')
    plt.show()


# ['normal_0.jpg', 'normal_1.jpg', 'normal_10.jpg', 'normal_100.jpg', 'normal_101.jpg', 'normal_102.jpg', 'normal_103.jpg', 'normal_104.jpg', 'normal_105.jpg', 'normal_106.jpg', 'normal_107.jpg', 'normal_108.jpg', 'normal_109.jpg', 'normal_11.jpg', 'normal_110.jpg', 'normal_111.jpg', 'normal_112.jpg', 'normal_113.jpg', 'normal_114.jpg', 'normal_115.jpg', 'normal_116.jpg', 'normal_117.jpg', 'normal_118.jpg', 'normal_119.jpg', 'normal_12.jpg', 'normal_120.jpg', 'normal_121.jpg', 'normal_122.jpg', 'normal_123.jpg', 'normal_124.jpg', 'normal_125.jpg', 'normal_126.jpg', 'normal_127.jpg', 'normal_128.jpg', 'normal_129.jpg', 'normal_13.jpg', 'normal_130.jpg', 'normal_131.jpg', 'normal_14.jpg', 'normal_15.jpg', 'normal_16.jpg', 'normal_17.jpg', 'normal_18.jpg', 'normal_19.jpg', 'normal_2.jpg', 'normal_20.jpg', 'normal_21.jpg', 'normal_22.jpg', 'normal_23.jpg', 'normal_24.jpg', 'normal_25.jpg', 'normal_26.jpg', 'normal_27.jpg', 'normal_28.jpg', 'normal_29.jpg', 'normal_3.jpg', 'normal_30.jpg', 'normal_31.jpg', 'normal_32.jpg', 'normal_33.jpg', 'normal_34.jpg', 'normal_35.jpg', 'normal_36.jpg', 'normal_37.jpg', 'normal_38.jpg', 'normal_39.jpg', 'normal_4.jpg', 'normal_40.jpg', 'normal_41.jpg', 'normal_42.jpg', 'normal_43.jpg', 'normal_44.jpg', 'normal_45.jpg', 'normal_46.jpg', 'normal_47.jpg', 'normal_48.jpg', 'normal_49.jpg', 'normal_5.jpg', 'normal_50.jpg', 'normal_51.jpg', 'normal_52.jpg', 'normal_53.jpg', 'normal_54.jpg', 'normal_55.jpg', 'normal_56.jpg', 'normal_57.jpg', 'normal_58.jpg', 'normal_59.jpg', 'normal_6.jpg', 'normal_60.jpg', 'normal_61.jpg', 'normal_62.jpg', 'normal_63.jpg', 'normal_64.jpg', 'normal_65.jpg', 'normal_66.jpg', 'normal_67.jpg', 'normal_68.jpg', 'normal_69.jpg', 'normal_7.jpg', 'normal_70.jpg', 'normal_71.jpg', 'normal_72.jpg', 'normal_73.jpg', 'normal_74.jpg', 'normal_75.jpg', 'normal_76.jpg', 'normal_77.jpg', 'normal_78.jpg', 'normal_79.jpg', 'normal_8.jpg', 'normal_80.jpg', 'normal_81.jpg', 'normal_82.jpg', 'normal_83.jpg', 'normal_84.jpg', 'normal_85.jpg', 'normal_86.jpg', 'normal_87.jpg', 'normal_88.jpg', 'normal_89.jpg', 'normal_9.jpg', 'normal_90.jpg', 'normal_91.jpg', 'normal_92.jpg', 'normal_93.jpg', 'normal_94.jpg', 'normal_95.jpg', 'normal_96.jpg', 'normal_97.jpg', 'normal_98.jpg', 'normal_99.jpg']
normal = [0.15, 0.11, 0.11, 0.11, 0.12, 0.16, 0.12, 0.13, 0.12, 0.11, 0.12, 0.12, 0.13, 0.59, 0.42, 0.12, 0.12, 0.12, 0.11, 0.12, 0.12, 0.12, 0.12, 0.11, 0.59, 0.11, 0.2, 0.12, 0.72, 0.12, 0.11, 0.12, 0.11, 0.19, 0.12, 0.13, 0.12, 0.12, 0.12, 0.97, 0.23, 0.31, 0.11, 0.11, 0.18, 0.21, 0.17, 0.22, 0.13, 0.11, 0.91, 0.19, 0.17, 0.47, 0.12, 0.2, 0.12, 0.12, 0.59, 0.12, 0.12, 0.12, 0.22, 0.16, 0.2, 0.25, 0.11, 0.12, 0.12, 0.15, 0.11, 0.17, 0.12, 0.11, 0.14, 0.14, 0.12, 0.62, 0.12, 0.21, 0.11, 0.12, 0.12, 0.11, 0.13, 0.14, 0.12, 0.12, 0.11, 0.12, 0.16, 0.12, 0.22, 0.11, 0.14, 0.12, 0.12, 0.12, 0.12, 0.13, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.11, 0.17, 0.22, 0.12, 0.16, 0.2, 0.11, 0.12, 0.15, 0.11, 0.15, 0.13, 0.13, 0.12, 0.12, 0.14, 0.12, 0.12, 0.12, 0.11, 0.12, 0.12, 0.12, 0.12, 0.12]
# ['sep1-C-0.jpg', 'sep1-C-1.jpg', 'sep1-C-10.jpg', 'sep1-C-11.jpg', 'sep1-C-2.jpg', 'sep1-C-3.jpg', 'sep1-C-4.jpg', 'sep1-C-5.jpg', 'sep1-C-6.jpg', 'sep1-C-7.jpg', 'sep1-C-8.jpg', 'sep1-C-9.jpg']
sep1_C = [0.49, 0.47, 0.53, 0.45, 0.39, 0.47, 0.5, 0.7, 0.4, 0.39, 0.67, 0.42]
# ['sep1-V-0.jpg', 'sep1-V-1.jpg', 'sep1-V-10.jpg', 'sep1-V-11.jpg', 'sep1-V-12.jpg', 'sep1-V-13.jpg', 'sep1-V-14.jpg', 'sep1-V-2.jpg', 'sep1-V-3.jpg', 'sep1-V-4.jpg', 'sep1-V-5.jpg', 'sep1-V-6.jpg', 'sep1-V-7.jpg', 'sep1-V-8.jpg', 'sep1-V-9.jpg']
sep1_V = [0.4, 0.32, 0.27, 0.4, 0.45, 0.41, 0.28, 0.35, 0.26, 0.29, 0.25, 0.25, 0.41, 0.31, 0.25]
# ['sep2-C-0.jpg', 'sep2-C-1.jpg', 'sep2-C-10.jpg', 'sep2-C-11.jpg', 'sep2-C-12.jpg', 'sep2-C-13.jpg', 'sep2-C-14.jpg', 'sep2-C-15.jpg', 'sep2-C-16.jpg', 'sep2-C-17.jpg', 'sep2-C-18.jpg', 'sep2-C-19.jpg', 'sep2-C-2.jpg', 'sep2-C-20.jpg', 'sep2-C-21.jpg', 'sep2-C-22.jpg', 'sep2-C-23.jpg', 'sep2-C-24.jpg', 'sep2-C-25.jpg', 'sep2-C-26.jpg', 'sep2-C-27.jpg', 'sep2-C-28.jpg', 'sep2-C-29.jpg', 'sep2-C-3.jpg', 'sep2-C-30.jpg', 'sep2-C-31.jpg', 'sep2-C-32.jpg', 'sep2-C-4.jpg', 'sep2-C-5.jpg', 'sep2-C-6.jpg', 'sep2-C-7.jpg', 'sep2-C-8.jpg', 'sep2-C-9.jpg']
sep2_C = [0.41, 0.32, 0.32, 0.42, 0.5, 0.33, 0.3, 0.29, 0.29, 0.3, 0.3, 0.28, 0.32, 0.4, 0.34, 0.34, 0.43, 0.32, 0.57, 0.39, 0.39, 0.35, 0.39, 0.37, 0.47, 0.5, 0.51, 0.41, 0.39, 0.32, 0.46, 0.29, 0.41]
# ['sep2-V-0.jpg', 'sep2-V-1.jpg', 'sep2-V-10.jpg', 'sep2-V-11.jpg', 'sep2-V-12.jpg', 'sep2-V-13.jpg', 'sep2-V-14.jpg', 'sep2-V-15.jpg', 'sep2-V-16.jpg', 'sep2-V-17.jpg', 'sep2-V-18.jpg', 'sep2-V-19.jpg', 'sep2-V-2.jpg', 'sep2-V-20.jpg', 'sep2-V-21.jpg', 'sep2-V-22.jpg', 'sep2-V-23.jpg', 'sep2-V-24.jpg', 'sep2-V-25.jpg', 'sep2-V-26.jpg', 'sep2-V-27.jpg', 'sep2-V-28.jpg', 'sep2-V-29.jpg', 'sep2-V-3.jpg', 'sep2-V-4.jpg', 'sep2-V-5.jpg', 'sep2-V-6.jpg', 'sep2-V-7.jpg', 'sep2-V-8.jpg', 'sep2-V-9.jpg']
sep2_V = [0.74, 0.23, 0.24, 0.21, 0.2, 0.23, 0.32, 0.23, 0.3, 0.24, 0.19, 0.23, 0.2, 0.21, 0.3, 0.19, 0.28, 0.25, 0.24, 0.2, 0.39, 0.29, 0.2, 0.2, 0.19, 0.19, 0.29, 0.23, 0.26, 0.41]
# ['sep3-C-0.jpg', 'sep3-C-1.jpg', 'sep3-C-10.jpg', 'sep3-C-11.jpg', 'sep3-C-12.jpg', 'sep3-C-13.jpg', 'sep3-C-14.jpg', 'sep3-C-15.jpg', 'sep3-C-16.jpg', 'sep3-C-17.jpg', 'sep3-C-2.jpg', 'sep3-C-3.jpg', 'sep3-C-4.jpg', 'sep3-C-5.jpg', 'sep3-C-6.jpg', 'sep3-C-7.jpg', 'sep3-C-8.jpg', 'sep3-C-9.jpg']
sep3_C = [0.03, 0.03, 0.04, 0.02, 0.02, 0.03, 0.05, 0.04, 0.03, 0.12, 0.03, 0.03, 0.02, 0.02, 0.02, 0.03, 0.03, 0.02]
# ['sep3-V-0.jpg', 'sep3-V-1.jpg', 'sep3-V-10.jpg', 'sep3-V-11.jpg', 'sep3-V-12.jpg', 'sep3-V-13.jpg', 'sep3-V-14.jpg', 'sep3-V-15.jpg', 'sep3-V-16.jpg', 'sep3-V-17.jpg', 'sep3-V-18.jpg', 'sep3-V-19.jpg', 'sep3-V-2.jpg', 'sep3-V-20.jpg', 'sep3-V-21.jpg', 'sep3-V-22.jpg', 'sep3-V-23.jpg', 'sep3-V-24.jpg', 'sep3-V-25.jpg', 'sep3-V-3.jpg', 'sep3-V-4.jpg', 'sep3-V-5.jpg', 'sep3-V-6.jpg', 'sep3-V-7.jpg', 'sep3-V-8.jpg', 'sep3-V-9.jpg']
sep3_V = [0.64, 0.76, 0.55, 0.45, 0.46, 0.56, 0.64, 0.66, 0.81, 0.66, 0.53, 0.48, 0.5, 0.48, 0.51, 0.53, 0.61, 0.59, 0.43, 0.67, 0.49, 0.51, 0.49, 0.73, 0.67, 0.63]
# ['sep4-C-0.jpg', 'sep4-C-1.jpg', 'sep4-C-10.jpg', 'sep4-C-2.jpg', 'sep4-C-3.jpg', 'sep4-C-4.jpg', 'sep4-C-5.jpg', 'sep4-C-6.jpg', 'sep4-C-7.jpg', 'sep4-C-8.jpg', 'sep4-C-9.jpg']
sep4_C = [0.37, 0.38, 0.35, 0.35, 0.76, 0.42, 0.42, 0.54, 0.45, 0.39, 0.61]
# ['sep4-V-0.jpg', 'sep4-V-1.jpg', 'sep4-V-10.jpg', 'sep4-V-11.jpg', 'sep4-V-12.jpg', 'sep4-V-13.jpg', 'sep4-V-2.jpg', 'sep4-V-3.jpg', 'sep4-V-4.jpg', 'sep4-V-5.jpg', 'sep4-V-6.jpg', 'sep4-V-7.jpg', 'sep4-V-8.jpg', 'sep4-V-9.jpg']
sep4_V = [0.46, 0.33, 0.31, 0.34, 0.33, 0.34, 0.39, 0.55, 0.32, 0.3, 0.38, 0.66, 0.32, 0.34]

mutation = []
mutation.append(sep1_C)
mutation.append(sep1_V)
mutation.append(sep2_C)
mutation.append(sep2_V)
mutation.append(sep3_C)
mutation.append(sep3_V)
mutation.append(sep4_C)
mutation.append(sep4_V)

standardError(normal, mutation)