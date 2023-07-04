import { useState } from "react";
import axios from "axios";
import { Navigate } from "react-router-dom";

export const Register = () => {

  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [navigate, setNavigate] = useState(false);

  const submit=async e=>{
    e.preventDefault();
    await axios.post('http://localhost:8000/account/register',{
      name,
      email,
      password
    })
    
    setNavigate(true);

  } 
  
  if(navigate){
    return <Navigate to="/login" />
  }

    return <main className="form-signin w-100 m-auto">
          <form onSubmit={submit}>        
            <h1 className="h3 mb-3 fw-normal">Please Register</h1>
              <div className="form-floating">
                <input type="text" className="form-control" id="floatingInput" placeholder="Name"
                  onChange={(e) => setName(e.target.value)}
                />
                <label>Name</label>
              </div>
              <div className="form-floating">
                <input type="email" className="form-control" id="floatingInput" placeholder="name@example.com"
                  onChange={(e) => setEmail(e.target.value)}
                />
                <label htmlFor="floatingInput">Email address</label>
              </div>
              <div className="form-floating">
                <input type="password" className="form-control" id="floatingPassword" placeholder="Password"
                  onChange={e => setPassword(e.target.value)}
                />
                <label for="floatingPassword">Password</label>
              </div>
    
              <button className="btn btn-primary w-100 py-2" type="submit">Submit</button>
          </form>
        </main>
}