import { createSlice, PayloadAction } from '@reduxjs/toolkit';

// Notification type for displaying toast messages
export interface Notification {
  id: string;
  message: string;
  type: 'success' | 'error' | 'info' | 'warning';
  timeout?: number;
}

// Interface for the UI state slice
interface UiState {
  isLoading: boolean;
  activeModal: string | null;
  modalData: Record<string, any> | null;
  notifications: Notification[];
  sidebarOpen: boolean;
}

// Initial state
const initialState: UiState = {
  isLoading: false,
  activeModal: null,
  modalData: null,
  notifications: [],
  sidebarOpen: false,
};

// Create the slice
const uiSlice = createSlice({
  name: 'ui',
  initialState,
  reducers: {
    // Loading state actions
    setLoading: (state, action: PayloadAction<boolean>) => {
      state.isLoading = action.payload;
    },
    
    // Modal actions
    openModal: (state, action: PayloadAction<{ modalId: string; data?: Record<string, any> }>) => {
      state.activeModal = action.payload.modalId;
      state.modalData = action.payload.data || null;
    },
    closeModal: (state) => {
      state.activeModal = null;
      state.modalData = null;
    },
    
    // Notification actions
    addNotification: (state, action: PayloadAction<Omit<Notification, 'id'>>) => {
      const id = Date.now().toString();
      state.notifications.push({
        id,
        ...action.payload,
      });
    },
    removeNotification: (state, action: PayloadAction<string>) => {
      state.notifications = state.notifications.filter(
        (notification) => notification.id !== action.payload
      );
    },
    clearNotifications: (state) => {
      state.notifications = [];
    },
    
    // Sidebar toggle
    toggleSidebar: (state) => {
      state.sidebarOpen = !state.sidebarOpen;
    },
    setSidebarOpen: (state, action: PayloadAction<boolean>) => {
      state.sidebarOpen = action.payload;
    },
  },
});

// Export actions
export const {
  setLoading,
  openModal,
  closeModal,
  addNotification,
  removeNotification,
  clearNotifications,
  toggleSidebar,
  setSidebarOpen,
} = uiSlice.actions;

// Export reducer
export default uiSlice.reducer; 