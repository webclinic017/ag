import React from "react";
import "./App.css";
import { AppContextProvider } from "./AppContext";
import Layout from "./components/Layout";

function App() {
  	return (
		  <AppContextProvider>
			  <Layout></Layout>
		  </AppContextProvider>
	  );
}

export default App;
