import React from "react";
import { Link, useNavigate } from "react-router-dom";
import { getToken, removeToken } from "../Services/LocalStorageServices";
import { useSnackbar } from "notistack";
export const Sidebar = () => {
  const navigate = useNavigate();
  const { enqueueSnackbar } = useSnackbar();
  const { access_token, refresh_token } = getToken();
  const handleLogout = async () => {
    try {
      const form = new FormData();
      form.append("refresh_token", refresh_token);
      //dispatch(signOutUserStart());
      const res = await fetch(
        `${process.env.REACT_APP_API_URL}/accounts/logout/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${access_token}`,
          },
          body: form,
        }
      );
      console.log("res", res);
      const data = await res.json();
      console.log("data", data);

      if (data) {
        const { user_data } = data;
        await removeToken();
        localStorage.removeItem("id");
        //dispatch(signOutUserSuccess(user_data));
        navigate("/");
        enqueueSnackbar(data.msg, { variant: "success" });
      }
    } catch (error) {
      //dispatch(signOutUserFail());
      enqueueSnackbar(error.message, { variant: "error" });
    }
  };
  return (
    <nav id="menu" className="navbar navbar-default navbar-fixed-top">
      <div className="container">
        <div className="navbar-header">
          <button
            type="button"
            className="navbar-toggle collapsed"
            data-toggle="collapse"
            data-target="#bs-example-navbar-collapse-1"
          >
            {" "}
            <span className="sr-only">Toggle navigation</span>{" "}
            <span className="icon-bar"></span>{" "}
            <span className="icon-bar"></span>{" "}
            <span className="icon-bar"></span>{" "}
          </button>
          <a className="navbar-brand page-scroll" href="#page-top">
            IdenHills
          </a>{" "}
        </div>

        <div
          className="collapse navbar-collapse"
          id="bs-example-navbar-collapse-1"
        >
          <ul className="nav navbar-nav navbar-right">
            <li>
              <Link to={"/AddSliders"}>Add Sliders</Link>
            </li>
            <li>
              <Link to={"/AddClientSliders"}>Add Client Slider</Link>
            </li>

            <li>
              <Link onClick={handleLogout} to="/">
                logOut
              </Link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  );
};
