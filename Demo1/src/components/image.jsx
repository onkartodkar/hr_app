import React, { useEffect, useRef } from "react";

export const Image = (props) => {
  const { data } = props;
  const containerRef = useRef(null);

  useEffect(() => {
    // Automatically scroll the container horizontally
    const intervalId = setInterval(() => {
      if (containerRef.current) {
        containerRef.current.scrollLeft += 1; // Adjust the scroll speed as needed
      }
    }, 30); // Adjust the scroll interval as needed

    // Clean up the interval on component unmount
    return () => clearInterval(intervalId);
  }, []); // Run this effect only once on component mount

  if (!data || !Array.isArray(data) || data.length === 0) {
    return null; // Render nothing if data is undefined, not an array, or empty
  }

  return (
    <div id="gallery">
      <h1 style={{ textAlign: "center" }}>Our Clients</h1>
      <div
        ref={containerRef}
        style={{
          display: "flex",
          overflowX: "auto",
          gap: "10px",
          padding: "10px",
        }}
      >
        {data.map((item) => (
          <div
            key={item.id}
            style={{
              position: "relative",
              textAlign: "center",
              //color: "white",
              minWidth: "200px",
              maxWidth: "200px",
              height: "250px",
              overflow: "hidden",
              padding: "10px",
              margin: "0 auto",
              borderRadius: "5px",
              boxShadow: "0px 0px 5px rgba(0, 0, 0, 0.3)",
              WebkitOverflowScrolling: "touch", // For smoother scrolling on iOS devices
              scrollbarWidth: "none", // Firefox
              msOverflowStyle: "none", // Internet Explorer and Edge
              "&::-webkit-scrollbar": {
                display: "none", // Hide scrollbar for WebKit browsers (Chrome, Safari)
              },
            }}
          >
            <img
              src={`http://192.168.0.106:8001${item.image}`}
              alt={item.title}
              style={{ width: "100%", height: "100%", objectFit: "cover" }}
            />
            <div
              style={{
                position: "absolute",
                backgroundColor: "black",
                top: "90%",
                left: "50%",
                transform: "translate(-50%, -50%)",
                width: "100%",
                padding: "5px",
                opacity: "0.6",
                fontSize: "16px",
                fontWeight: "bold",
                textAlign: "center",

                textShadow: "1px 1px 2px rgba(0, 0, 0, 0.3)",
              }}
            >
              <div style={{ color: "white" }}>{item.title}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};
