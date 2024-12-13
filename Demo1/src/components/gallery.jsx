import React from "react";
import { Image } from "./image";

export const Gallery = (props) => {
  console.log(props.data);
  const { clients } = props.data;
  console.log(clients);
  return (
    <div>
      <Image data={clients} />
    </div>
  );
};
