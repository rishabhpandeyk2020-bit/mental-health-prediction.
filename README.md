# Mental Health Prediction API

## Authentication
JWT/token authentication has been removed.

Registration and login still validate the user's email/password. Login returns the `user_id`, which must be supplied to prediction/history APIs.

## Prediction

POST `/predict/{user_id}`

The prediction is saved in `prediction_history.user_id` for the supplied user.

## History

GET `/history/user/{user_id}` - get all predictions for a user.

GET `/history/user/{user_id}/{history_id}` - get one prediction belonging to that user.

DELETE `/history/user/{user_id}/{history_id}` - delete one prediction belonging to that user.

DELETE `/history/user/{user_id}` - delete all predictions belonging to that user.

## Example flow

1. POST `/auth/login` and get `user_id`.
2. POST `/predict/{user_id}` with the prediction data.
3. GET `/history/user/{user_id}` to load that user's prediction history.
