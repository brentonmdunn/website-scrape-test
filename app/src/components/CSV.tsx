// interface CSVProp {
//   event:
// }

export const CSV = () => {
  const changeHandler = (event: React.ChangeEvent<{ value: unknown }>) => {
    const value = event.target.value;

    console.log(value);
  };

  return (
    <div>
      <h1>TEXT</h1>
      <input
        type="file"
        name="file"
        accept=".csv"
        onChange={changeHandler}
        style={{ display: "block", margin: "10px auto" }}
      />
    </div>
  );
};
