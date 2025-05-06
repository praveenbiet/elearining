import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';
import { apiTags } from './tags';
import { appConfig } from '../config';

// Base API setup for RTK Query
export const baseApi = createApi({
  reducerPath: 'api',
  baseQuery: fetchBaseQuery({
    baseUrl: appConfig.API_URL,
    prepareHeaders: (headers, { getState }) => {
      // Get token from auth state
      const token = (getState() as any).auth.token;
      
      // Add authorization header if token exists
      if (token) {
        headers.set('Authorization', `Bearer ${token}`);
      }
      
      // Add content type for JSON
      headers.set('Content-Type', 'application/json');
      
      return headers;
    },
  }),
  // Cache tag types for invalidation
  tagTypes: apiTags,
  // Empty base endpoints - will be injected by feature slices
  endpoints: () => ({}),
}); 