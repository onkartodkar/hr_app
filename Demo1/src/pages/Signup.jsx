import React from "react";
import { useState } from "react";
import { Link } from "react-router-dom";
import { useSnackbar } from "notistack";
const Signup = () => {
  const { enqueueSnackbar } = useSnackbar();
  const [formData, setFormData] = useState({
    user_name: "",
    email: "",
    phone_number: "",
    password: "",
    confirm_password: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    // Here you can add your form submission logic
    console.log("Form submitted:", formData);
    const res = await fetch(
      `${process.env.REACT_APP_API_URL}/accounts/register/`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      }
    );
    const data = await res.json();
    if (data.error && data.error.email) {
      enqueueSnackbar(data.error.email[0], { variant: "error" });
    } else if (data.error && data.error.phone_number) {
      enqueueSnackbar(data.error.phone_number[0], { variant: "error" });
    } else if (data.error && data.error.password) {
      enqueueSnackbar(data.error.password[0], { variant: "error" });
    } else if (data.error && data.error.user_name) {
      enqueueSnackbar(data.error.user_name[0], { variant: "error" });
    } else if (data.error && data.error.confirm_password) {
      enqueueSnackbar(data.error.confirm_password[0], { variant: "error" });
    } else {
      enqueueSnackbar("Successfully registered.. please login", {
        variant: "success",
      });
    }
    // Reset form fields after submission if needed
  };
  return (
    <div>
      <div id="contact">
        <div className="container">
          <div className="col-md-8">
            <div className="row">
              <div className="section-title">
                <h2>Sign-Up</h2>
              </div>
              <form noValidate onSubmit={handleSubmit}>
                <div className="row">
                  <div className="col-md-6">
                    <div className="form-group">
                      <input
                        type="text"
                        name="user_name"
                        className="form-control"
                        placeholder="UserName"
                        required
                        onChange={handleChange}
                      />
                      <p className="help-block text-danger"></p>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-group">
                      <input
                        type="email"
                        name="email"
                        className="form-control"
                        placeholder="Email"
                        required
                        onChange={handleChange}
                      />
                      <p className="help-block text-danger"></p>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-group">
                      <input
                        type="number"
                        name="phone_number"
                        className="form-control"
                        placeholder="Phone Number"
                        required
                        onChange={handleChange}
                      />
                      <p className="help-block text-danger"></p>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-group">
                      <input
                        type="password"
                        name="password"
                        className="form-control"
                        placeholder="password"
                        required
                        onChange={handleChange}
                      />
                      <p className="help-block text-danger"></p>
                    </div>
                  </div>
                  <div className="col-md-6">
                    <div className="form-group">
                      <input
                        type="password"
                        name="confirm_password"
                        className="form-control"
                        placeholder="confirm password"
                        required
                        onChange={handleChange}
                      />
                      <p className="help-block text-danger"></p>
                    </div>
                  </div>
                </div>
                <button type="submit" className="btn btn-custom btn-lg">
                  Sign-Up
                </button>
              </form>
            </div>
            <div className="row">
              <p className="text-white">
                <Link
                  style={{ color: "white" }}
                  className="text-white"
                  to={"/sign-in"}
                >
                  Already Have An Account ? Sign-in Here
                </Link>
              </p>
            </div>
          </div>
        </div>
        <div className="container"></div>
      </div>
    </div>
  );
};

export default Signup;
