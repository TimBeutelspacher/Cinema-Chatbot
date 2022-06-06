import './App.css';
import Basic from "./components/Basic"

function App() {
  return (
    <div class="outer">
      <div class="middle">
        <div class="inner"></div>
          <div className="App">
            <h1>NLP Projekt - SS22</h1>
            <h5>von Tim Beutelspacher</h5>
            <div className='spareBox'></div>
            <Basic />
          </div>
        </div>
      </div>
  );
}

export default App;
