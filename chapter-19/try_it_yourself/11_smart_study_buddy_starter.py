# Smart Study Buddy (capstone)
# 1) Load ../data/student_habits.csv
# 2) Clean invalid rows (negative study, >24h sleep/social)
# 3) Train KNN (k=3) on [study_hours, sleep_hours, social_media_hours] -> grade
# 4) Ask for a new plan and predict; print confidence + suggestions.
import numpy as np
import pandas as pd
# TODO: your code here
