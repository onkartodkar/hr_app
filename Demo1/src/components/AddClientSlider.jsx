import React from "react";
import { Link } from "react-router-dom";
import { enqueueSnackbar, useSnackbar } from "notistack";
import { useState } from "react";
import { getToken } from "../Services/LocalStorageServices";
const AddClientSlider = () => {
  const { enqueueSnackbar } = useSnackbar();
  const access_token = getToken();
  const [formData, setFormData] = useState({
    title: "",
    text: "",
    image: null,
    office_staff: localStorage.getItem("id"),
  });

  const handleChange = (event) => {
    const { name, value, files } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: name === "image" ? files[0] : value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formDataToSend = new FormData();
    formDataToSend.append("title", formData.title);
    formDataToSend.append("text", formData.text);
    /*formData.image.forEach((file, index) => {
          formDataToSend.append(`image${index}`, file);
        });*/
    formDataToSend.append("image", formData.image);
    formDataToSend.append("office_staff", formData.office_staff);

    try {
      const response = await fetch(
        `${process.env.REACT_APP_API_URL}/add_client/`,
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${access_token.access_token}`,
          },
          body: formDataToSend,
        }
      );
      console.log("token", access_token.access_token);
      const data = await response.json();
      console.log("data", data);

      // Reset form data after submission
      setFormData({
        title: "",
        text: "",
        image: "",
        office_staff: localStorage.getItem("id"),
      });
      if (
        (data.error && data.error.image[0]) ||
        (data.error && data.error.text[0]) ||
        (data.error && data.error.title[0])
      ) {
        //setLoading(false);
        enqueueSnackbar(
          <p>
            {data.error.image[0] || data.error.text[0] || data.error.title[0]}
          </p>,
          {
            variant: "error",
          }
        );
        return;
      }
      if (data.msg && data.msg) {
        enqueueSnackbar(<p>{data.msg}</p>, { variant: "success" });
      }
    } catch {
      enqueueSnackbar("Enter the fields now", { variant: "error" });
    }
  };

  console.log(formData);

  return (
    <div>
      <div className="row">
        <div className="section-title">
          <h2>Add Sliders</h2>
        </div>
      </div>
      <div className="container d-flex">
        <div className="col-md-6">
          <div className="section-title">
            <h1>Add Client Sliders</h1>
          </div>
          <form onSubmit={handleSubmit}>
            <div className="mb-3">
              <label htmlFor="exampleInputEmail1" className="form-label">
                Slider Title
              </label>
              <input
                type="text"
                className="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
                name="title"
                value={formData.title}
                onChange={handleChange}
                required
              />
            </div>
            <div className="mb-3">
              <label htmlFor="exampleInputPassword1" className="form-label">
                Slider Text
              </label>
              <textarea
                className="form-control"
                placeholder="write text here"
                id="floatingTextarea"
                name="text"
                value={formData.text}
                onChange={handleChange}
                required
              ></textarea>
            </div>
            <div className="mb-3">
              <label className="input-group-text" htmlFor="inputGroupFile01">
                Upload Images
              </label>
              <input
                type="file"
                className="form-control"
                multiple
                accept="image/*"
                id="inputGroupFile01"
                name="image"
                onChange={handleChange}
                required
              />
            </div>
            <br />
            <button type="submit" className="btn btn-primary">
              Submit
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default AddClientSlider;
