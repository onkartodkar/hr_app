import { configureStore } from "@reduxjs/toolkit";
import userStore from "./userSlice";

const appStore = configureStore({
  reducer: {
    user: userStore,
  },
});
export default appStore;
