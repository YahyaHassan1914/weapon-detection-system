import "./Details.css";
import ReactPlayer from "react-player";

function DetailsPage({ onBackClicked, url, date }) {
  return (
    <div className="details-page">
      <button onClick={onBackClicked} className="back-btn">
        Back
      </button>
      <h3>Weapon Detected</h3>
      <ReactPlayer url={url} controls={true} />
      <p>{date}</p>
    </div>
  );
}

export default DetailsPage;
