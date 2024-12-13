import React from "react";
import { Swiper, SwiperSlide } from "swiper/react";
import { Pagination, Autoplay } from "swiper/modules";
import "swiper/css";
import "swiper/css/pagination";
//import { Autoplay, Pagination } from 'swiper/modules';

export const Header = (props) => {
  // console.log(props.data.clients[0].title);

  const { heros } = props.data;
  console.log(heros);

  return (
    <div>
      <Swiper
        pagination={{
          dynamicBullets: true,
          clickable: true,
        }}
        spaceBetween={30}
        centeredSlides={true}
        autoplay={{
          delay: 2500,
          disableOnInteraction: false,
        }}
        modules={[Pagination, Autoplay]}
        className="mySwiper my-5"
      >
        {heros?.map((homeAd) => (
          <SwiperSlide key={homeAd.id} className="swiper-slide">
            <div className="swiper-slide-content">
              <div className="overlay"></div>
              <div className="overlay">
                <h1
                  style={{
                    fontSize: "6em",
                    fontWeight: "bold",
                    color: "white",
                  }}
                >
                  {homeAd.title}
                </h1>
                <p
                  style={{
                    // fontSize: "1em",
                    fontWeight: "bold",
                    color: "white",
                  }}
                >
                  {homeAd.text}
                </p>
              </div>
              <img
                src={`http://192.168.0.106:8001/${homeAd?.image}`}
                alt={homeAd.id}
                style={{
                  width: "100vw", // Set width to 100% of viewport width
                  height: "auto", // Fixed height of 300px
                  objectFit: "cover", // Maintain aspect ratio and cover the entire container
                  borderRadius: "10px", // Add rounded corners
                  boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)", // Add a subtle shadow
                  transition: "transform 0.2s ease-in-out", // Add smooth hover effect
                }}
              />
            </div>
          </SwiperSlide>
        ))}
      </Swiper>
    </div>
  );
};
