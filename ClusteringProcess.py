from keras.applications import VGG16
from sklearn.cluster import AgglomerativeClustering, KMeans
from keras.layers import Dense, Dropout, GlobalAveragePooling2D
from keras.models import Model
from keras.preprocessing.image import load_img, img_to_array
import numpy as np
import seaborn as sns
import os
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from munkres import Munkres, print_matrix
import sys
from sklearn.decomposition import PCA


base_model = VGG16(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
inputShape = (224, 224, 3)  # Assumes 3 channel image

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(512, activation="relu")(x)
x = Dropout(0.3)(x)
x = Dense(512, activation="relu")(x)
predictions = Dense(9, activation='softmax')(x)
model = Model(inputs=base_model.input, outputs=predictions)

# Need use this weight file, I put it on the one-drive
model.load_weights("GAP_D_Drop_D_D.h5")

# The flower data is on the one-drive
dirname_path = 'test_data'

t = 0
cluster_number = 9
true_label = []
vgg16_feature_list = []
rawImage_list = []
dir_path_list = os.listdir(dirname_path)
if '.DS_Store' in dir_path_list:
    dir_path_list.remove('.DS_Store')
dir_path_list.sort()
class_item = 0
for dirname in dir_path_list:
    file_path = dirname_path + '/' + dirname
    file_path_list = os.listdir(file_path)
    if '.DS_Store' in file_path_list:
        file_path_list.remove('.DS_Store')
    file_path_list.sort()
    for filename in file_path_list:
        img_path = file_path + '/' + filename
        true_label.append(class_item)
        image = load_img(img_path, target_size=inputShape)
        image = img_to_array(image)  # shape is (224,224,3)
        feature_vectors = np.expand_dims(image, axis=0)  # Now shape is (1,224,224,3)
        feature_vectors = feature_vectors / 255.0
        preds = model.predict(feature_vectors)  # (1, 7, 7, 512). float32
        vgg16_feature_np = np.array(preds)  # (1, 7, 7, 512). array
        vgg16_feature_list.append(vgg16_feature_np.flatten())  # (n, 25088)

    class_item += 1

vgg16_feature_list_np = np.array(vgg16_feature_list)
clusters_features = KMeans(n_clusters=cluster_number).fit(vgg16_feature_list_np)
labels_features = clusters_features.labels_


# Munkres algorithm
def get_matrix(y_pred, y_true):
    cm_array = confusion_matrix(y_pred, y_true)
    # print("matrix: ", cm_array)
    cm_array_new = [[0 for i in range(cluster_number)] for i in range(cluster_number)]
    for row in range(len(cm_array[:][0])):
        for col in range(len(cm_array[0][:])):
            cm_array_new[row][col] = cm_array[row][col]
    print("new_matrix: ", cm_array_new)

    # Calculating Profit, Rather than Cost
    cost_matrix = []
    for row in cm_array_new:
        cost_row = []
        for col in row:
            cost_row += [sys.maxsize - col]
        cost_matrix += [cost_row]

    m = Munkres()
    indexes = m.compute(cost_matrix)
    print_matrix(cm_array_new, msg='Highest profit through this matrix:')
    total = 0
    prediction = []
    for row, column in indexes:
        value = cm_array_new[row][column]
        prediction.append(column)
        total += value
        print('(%d, %d) -> %d' % (row, column, value))

    print('total profit=%d' % total)

    return prediction


prediction_features = get_matrix(labels_features, true_label)


for i in range(len(labels_features)):
    labels_features[i] = prediction_features[labels_features[i]]


print('Truth: ', true_label)
print('Converted features Labels: ', labels_features)


normal_index = []
image_index =[]
mutation_index_1 =[]
mutation_index_2 =[]
mutation_index_3 =[]
mutation_index_4 =[]
mutation_index_5 =[]
mutation_index_6 =[]
mutation_index_7 =[]
mutation_index_8 =[]

normal_index.append([t for t, x in enumerate(true_label) if x == 0])
mutation_index_1.append([t for t, x in enumerate(true_label) if x == 1])
mutation_index_2.append([t for t, x in enumerate(true_label) if x == 2])
mutation_index_3.append([t for t, x in enumerate(true_label) if x == 3])
mutation_index_4.append([t for t, x in enumerate(true_label) if x == 4])
mutation_index_5.append([t for t, x in enumerate(true_label) if x == 5])
mutation_index_6.append([t for t, x in enumerate(true_label) if x == 6])
mutation_index_7.append([t for t, x in enumerate(true_label) if x == 7])
mutation_index_8.append([t for t, x in enumerate(true_label) if x == 8])

image_index.append(normal_index)
image_index.append(mutation_index_1)
image_index.append(mutation_index_2)
image_index.append(mutation_index_3)
image_index.append(mutation_index_4)
image_index.append(mutation_index_5)
image_index.append(mutation_index_6)
image_index.append(mutation_index_7)
image_index.append(mutation_index_8)


pca = PCA(n_components=2)     #输出两维
data_pca_list = pca.fit_transform(vgg16_feature_list_np)

for i, label in enumerate(labels_features):
    if label == 0:
        # normal flower
        plt.scatter(data_pca_list[i][0], data_pca_list[i][1], c='black')
    if label == 1:
        # sep1-C
        plt.scatter(data_pca_list[i][0], data_pca_list[i][1], c='blue')
    if label == 2:
        # sep1-V
        plt.scatter(data_pca_list[i][0], data_pca_list[i][1], c='brown')
    if label == 3:
        # sep2-C
        plt.scatter(data_pca_list[i][0], data_pca_list[i][1], c='green')
    if label == 4:
        # sep2-V
        plt.scatter(data_pca_list[i][0], data_pca_list[i][1], c='pink')
    if label == 5:
        # sep3-C
        plt.scatter(data_pca_list[i][0], data_pca_list[i][1], c='yellow')
    if label == 6:
        # sep3-V
        plt.scatter(data_pca_list[i][0], data_pca_list[i][1], c='skyblue')
    if label == 7:
        # sep4-C
        plt.scatter(data_pca_list[i][0], data_pca_list[i][1], c='purple')
    if label == 8:
        # sep4-V
        plt.scatter(data_pca_list[i][0], data_pca_list[i][1], c='red')

plt.tight_layout()
plt.savefig('Clustering.png')
plt.show()




