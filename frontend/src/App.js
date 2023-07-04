// import logo from './logo.svg';
import { Login } from './components/login';
import './App.css';

import {BrowserRouter,Routes,Route, Link} from 'react-router-dom';
import { Register } from './components/register';
import { Home } from './components/home';


function App() {
  return <BrowserRouter>
    <header className="p-3 text-bg-dark">
    <div className="container">
      <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">

        <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li><Link to="/"className="nav-link px-2 text-white">Home </Link></li>
        </ul>

        <div className="text-end">
          <Link to="/login" className="btn btn-outline-light me-2">Login</Link>
          <Link to="/register" className="btn btn-outline-light me-2">Register</Link>
        </div>
      </div>
    </div>
  </header>


    <Routes>
      <Route path="/" element={<Home/>}/>
      <Route path="/login" element={<Login/>}/>
      <Route path="/register" element={<Register/>}/>
    </Routes>
  </BrowserRouter>
}

export default App;
