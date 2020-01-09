image_predictions_clean['prediction'] = ""
image_predictions_clean['confidence_lvl'] = ""

def my_function(image_predictions_clean):
if image_predictions_clean['p1_dog'] == True:
        image_predictions_clean['prediction'].append(image_predictions_clean['p1'])
        image_predictions_clean['confidence_lvl'].append(image_predictions_clean['p1_conf'])
elif image_predictions_clean['p2_dog'] == True:
        image_predictions_clean['prediction'].append(image_predictions_clean['p2'])
        image_predictions_clean['confidence_lvl'].append(image_predictions_clean['p2_conf'])
elif image_predictions_clean['p3_dog'] == True:
        image_predictions_clean['prediction'].append(image_predictions_clean['p3'])
        image_predictions_clean['confidence_lvl'].append(image_predictions_clean['p3_conf'])
else:
        image_predictions_clean['prediction'].append('Nan')
        image_predictions_clean['confidence_lvl'].append(image_predictions_clean['0'])
