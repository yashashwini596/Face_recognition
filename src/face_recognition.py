import cv2
import os
import numpy as np


def extract_features(image_path):

    image = cv2.imread(image_path)

    if image is None:
        print("Failed to read:", image_path)
        return None

    image = cv2.resize(image,(100,100))

    features = image.flatten()

    return features


def compare_faces(test_image, dataset_folder):

    query_features = extract_features(test_image)

    if query_features is None:
        return "No face detected"

    best_match = None
    best_score = -1

    for person in os.listdir(dataset_folder):

        person_path = os.path.join(dataset_folder, person)

        for img in os.listdir(person_path):

            img_path = os.path.join(person_path, img)

            features = extract_features(img_path)

            if features is None:
                continue

            score = np.dot(query_features, features)

            if score > best_score:
                best_score = score
                best_match = person

    return best_match