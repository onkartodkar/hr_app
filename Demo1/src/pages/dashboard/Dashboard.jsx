import React from "react";
import { useState, useEffect } from "react";
import { Sidebar } from "../../components/sidebar";
import AddSliders from "../../components/AddSliders";
import AddClientSlider from "../../components/AddClientSlider";
/*import { Header } from "../../components/header";
import { Features } from "../../components/features";
import { Contact } from "../../components/contact";*/
import Signin from "../Signin";
import SmoothScroll from "smooth-scroll";
import { Outlet, Route, Router } from "react-router-dom";
export const scroll = new SmoothScroll('a[href*="dashboard/"]', {
  speed: 1000,
  speedAsDuration: true,
});
const Dashboard = () => {
  return (
    <div>
      <Sidebar />
      <Outlet />
    </div>
  );
};

export default Dashboard;
