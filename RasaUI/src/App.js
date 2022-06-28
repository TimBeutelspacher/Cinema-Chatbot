import './App.css';
import Basic from "./components/Basic"
import background from "./cinemaBackground.jpg";

function App() {
  return (
    <div class="outer" style={{
      backgroundImage: `url(${background})`,
      backgroundPosition: 'center',
      backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',
      width: '100vw',
      height: '100vh'
    }}>
      <div class="middle">
        <div class="inner"></div>
        <div className="App">
          <div className="head">
            <h1>NLP Projekt - SS22</h1>
            <h5>Tim Beutelspacher</h5>
          </div>
          <div className='spareBox'></div>
          <Basic />
        </div>
      </div>
    </div>
  );
}

export default App;
