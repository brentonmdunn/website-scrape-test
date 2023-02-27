import { useState } from "react";

export const Home = () => {
  const [data, setData] = useState([
    { department: "CSE", class: "8A", instructor: "Cao", id: 1 },
    { department: "BILD", class: "87", instructor: "Meaders", id: 2 },
    { department: "CAT", class: "1", instructor: "Bronstein", id: 3 },
  ]);

  return (
    <div>
      {data.map((datum) => (
        <div className="view-data" key={datum.id}>
          <h1>{datum.department}</h1>
          <h2>{datum.class}</h2>
          <h3>{datum.instructor}</h3>
        </div>
      ))}
    </div>
  );
};
