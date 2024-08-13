import React from 'react'
import { BrowserRouter, Routes } from 'react-router-dom'
import Home from './Components/Home';
import About from './Components/About';
import Portraits from './Components/Portraits';
import Documentary from './Components/Documentary';
import Albums from './Components/Albums';
import Blog from './Components/Blog';

function App() {
    return (
      <div>
        <BrowserRouter>
  
        <Routes>
          <Route path='/Home' element={<Home/>}/>
          <Route path='/About' element={<About category="About"/>}/>
          <Route path='/Portraits' element={<Portraits category="Portraits"/>}/>
          <Route path='/Documentary' element={<Documentary category="Documentary"/>}/>
          <Route path='/Albums' element={<Albums/>}/>
          <Route path='/Blog' element={<Blog/>}/>
        </Routes>
  
   
    </BrowserRouter>
  </div>
    );
  }

export default App