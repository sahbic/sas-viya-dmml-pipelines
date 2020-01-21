from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

from sasctl import Session
from sasctl.tasks import register_model


# Create X and y for training
X_train = dm_traindf.loc[:, dm_input]
y_train = dm_traindf[dm_dec_target]

# Preprocessing interval variables
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median'))])

# Preprocessing categorical variables
categorical_transformer = Pipeline(steps=[
     ('imputer', SimpleImputer(strategy='most_frequent')),
     ('onehot', OneHotEncoder(handle_unknown='ignore'))])

# Create preprocessing step
preprocessor = ColumnTransformer(transformers=[
    ('num', numeric_transformer, dm_interval_input),
    ('cat', categorical_transformer, dm_class_input)])

# Define pipeline steps
dm_model = Pipeline(steps=[
('preprocessor', preprocessor),
('model', GradientBoostingClassifier())])

fit = dm_model.fit(X_train, y_train)

# Score full data
scored = dm_model.predict_proba(dm_inputdf)
dm_scoreddf = pd.DataFrame(scored, columns=['P_' + dm_dec_target + level for level in dm_classtarget_level])

# Register model
with Session('http://sasserver.demo.sas.com', 'sasdemo', 'Orion123'):
    register_model(dm_model, 'OS Node sklearn', '4. Manage credit models', input=X_train)