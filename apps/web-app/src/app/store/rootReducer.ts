import { combineReducers } from '@reduxjs/toolkit';

// Import reducers from feature slices
import authReducer from '../../features/auth/model/slice';
import uiReducer from '../../shared/model/uiSlice';
import { baseApi } from '../../shared/api';

// Combine all reducers
const rootReducer = combineReducers({
  auth: authReducer,
  ui: uiReducer,
  [baseApi.reducerPath]: baseApi.reducer,
});

export default rootReducer; 