import React, { useState, useEffect } from "react";
import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";
/*import { Navigation } from "./components/navigation";
import { Header } from "./components/header";
import { Features } from "./components/features";
import { About } from "./components/about";
import { Services } from "./components/services";
import { Gallery } from "./components/gallery";
import { Testimonials } from "./components/testimonials";
import { Team } from "./components/Team";
import { Contact } from "./components/contact";
import Signin from "./components/Signin";
import JsonData from "./data/data.json";
import SmoothScroll from "smooth-scroll";*/
import "./App.css";
import Home from "./pages/Home";
import Signin from "./pages/Signin";
import Signup from "./pages/Signup";
import Dashboard from "./pages/dashboard/Dashboard";
import AddSliders from "./components/AddSliders";
import AddClientSlider from "./components/AddClientSlider";
const App = () => {
  const router = createBrowserRouter(
    createRoutesFromElements([
      <Route path="/" element={<Home />} />,
      <Route path="/sign-up" element={<Signup />} />,
      <Route path="/sign-in" element={<Signin />} />,
      <Route path="/" element={<Dashboard />}>
        <Route path="/AddSliders" element={<AddSliders />} />,
        <Route path="/AddClientSliders" element={<AddClientSlider />} />,
      </Route>,
    ])
  );
  return (
    /*<BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/sign-up" element={<Signup />} />
        <Route path="/sign-in" element={<Signin />} />
        <Route path="/dashboard" element={<Dashboard />}>
          <Route path="/AddSliders" element={<AddSliders />} />
          <Route path="/AddClientSliders" element={<AddClientSlider />} />
        </Route>
      </Routes>
    </BrowserRouter>*/
    <>
      <div>
        <RouterProvider router={router} />
      </div>
    </>
  );
};

export default App;
