# Lung Cancer Detection using Machine Learning

<p align="center">
  <img src="https://user-images.githubusercontent.com/83024561/226101378-c8fe7e92-796a-4a97-89a9-a0475c47a6e6.gif"
         alt="csi_logo">
</p>


- If lung cancer is found at an earlier stage, when it is small and before it has spread, it is more likely to be treated successfully. Lung cancer screening is recommended for certain people who smoke or used to smoke, but who don't have any signs or symptoms. If a person has lung cancer but doesn't have any symptoms, this usually means there's a chance to detect the disease early.

- Symptoms and the results of certain tests may strongly suggest that a person has lung cancer, but the actual diagnosis is made by looking at lung cells in the lab.

- The cells can be taken from lung secretions (mucus you cough up from the lungs), fluid removed from the area around the lung (thoracentesis), or from a suspicious area using a needle or surgery (biopsy). The choice of which test(s) to use depends on the situation.

- Check out the live Deployment at - [Streamlit Deployment](https://vedantkadam-lung-cancer-cnn-app-1hwc8w.streamlit.app/) 
## How to Run this Project

## Tech Stacks Used

- Python
- Streamlit API
- Tensorflow , Keras API
- Numpy , Pandas , Seaborn

## How to run this Project
```
git clone URL
```
```
cd LungCancerDetection
```

- Install modules if not available using following commands
```
pip install -r requirements.txt
```

- Run the app.py file
```
streamlit run app.py
```

- Note- Sometimes models as well as csv file might not be detected due to environment related issue it is recommended that you install Anaconda and create a seperate environment by the name 'tf' install required modules.
Then run the following commands-
```
activate conda tf
cd LungCancerDetection
streamlit run app.py

```

## UI Screenshots

- Home Page
<p align="center">
  <img src="https://user-images.githubusercontent.com/83024561/226101523-cc3cb8b6-49fe-4b79-a242-a55858ed1771.png"
         alt="csi_logo" width="800" height="400">
</p>

- Cancer Detected 
<p align="center">
  <img src="https://user-images.githubusercontent.com/83024561/226101529-275d64a7-c150-49e8-a63e-ce1c84b22235.png"
         alt="csi_logo" width="700" height="400">
</p>

- Normal Case 
<p align="center">
  <img src="https://user-images.githubusercontent.com/83024561/226101542-08bba1fa-fb17-4a02-b25f-9974ed7e1f95.png"
         alt="csi_logo" width="700" height="400">
</p>











