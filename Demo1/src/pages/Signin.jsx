import React from "react";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useSnackbar } from "notistack";
import { storeToken } from "../Services/LocalStorageServices";
const Signin = () => {
  const [formData, setFormData] = useState({});
  //const [loading, setLoading] = useState(false);

  const { enqueueSnackbar } = useSnackbar();

  const navigate = useNavigate();
  // const location = useLocation();
  //const dispatch = useDispatch();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
    console.log(formData);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    // const { password: pass, ...rest } = formData;
    try {
      //setLoading(true);
      //dispatch(signInStart());

      const res = await fetch(
        `${process.env.REACT_APP_API_URL}/accounts/login/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(formData),
        }
      );

      const data = await res.json();
      console.log("data", data);
      localStorage.setItem("id", data.data.user_id);
      storeToken(data.token);
      const { user_data } = data;
      //await dispatch(signInSuccess(user_data));
      if (data.error && data.error.non_field_errors) {
        //setLoading(false);
        enqueueSnackbar(<p>{data.error.non_field_errors[0]}</p>, {
          variant: "error",
        });
        return;
      }

      if (data.msg) {
        enqueueSnackbar(<p>{data.msg}</p>, { variant: "success" });

        //setLoading(false);
        console.log(data.msg);
      }
      setFormData("");
      navigate("/AddSliders");
      //setLoading(false);
    } catch (error) {
      //dispatch(signInFail());
      enqueueSnackbar("Enter the fields now", { variant: "error" });
      //setLoading(false);
    }
  };
  return (
    <div>
      <div id="contact">
        <div className="container">
          <div className="col-md-8">
            <div className="row">
              <div className="section-title">
                <h2>Sign In</h2>
              </div>
              <form no validate onSubmit={handleSubmit}>
                <div className="row">
                  <div className="col-md-6">
                    <div className="form-group">
                      <input
                        type="email"
                        id="email"
                        name="email"
                        className="form-control"
                        placeholder="Email"
                        required
                        onChange={handleChange}
                      />
                      <p className="help-block text-danger"></p>
                    </div>
                    <div className="form-group">
                      <input
                        type="password"
                        id="password"
                        name="password"
                        className="form-control"
                        placeholder="*******"
                        required
                        onChange={handleChange}
                      />
                      <p className="help-block text-danger"></p>
                    </div>
                  </div>
                </div>

                <div id="success"></div>
                <button type="submit" className="btn btn-custom btn-lg">
                  Sign-in
                </button>
              </form>
            </div>
            <div className="row">
              <p className="text-white">
                <Link
                  style={{ color: "black" }}
                  className="text-white"
                  to={"/sign-up"}
                >
                  Create An Account ? Sign-Up Here
                </Link>
              </p>
            </div>
          </div>

          <div className="col-md-12"></div>
        </div>
      </div>
    </div>
  );
};

export default Signin;
