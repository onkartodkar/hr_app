import { createSlice } from "@reduxjs/toolkit";

const userSlice = createSlice({
  name: "user",
  initialState: {
    allData: null,
  },
  reducers: {
    addUser: (state, action) => {
      state.allData = action.payload;
    },
  },
});
export const { addUser } = userSlice.actions;
export default userSlice.reducer;
