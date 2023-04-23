import React, { useState } from "react";
import axios from "axios";

function App() {
  const [businessName, setBusinessName] = useState("");
  const [yearEstablished, setYearEstablished] = useState("");
  const [loanAmount, setLoanAmount] = useState("");
  const [accountingProvider, setAccountingProvider] = useState("");
  const [decision, setDecision] = useState("");

  const handleSubmit = async (event) => {
    event.preventDefault();

    const application = {
      business_name: businessName,
      year_established: yearEstablished,
      loan_amount: loanAmount,
      accounting_provider: accountingProvider,
    };

    try {
      const response = await axios.post(
        "http://localhost:8000/application",
        application
      );
      setDecision(response.data.decision);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <div>
      <h1>Business Loan Application System</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Business Name:
          <input
            type="text"
            value={businessName}
            onChange={(event) => setBusinessName(event.target.value)}
          />
        </label>
        <br />
        <label>
          Year Established:
          <input
            type="text"
            value={yearEstablished}
            onChange={(event) => setYearEstablished(event.target.value)}
          />
        </label>
        <br />
        <label>
          Loan Amount:
          <input
            type="text"
            value={loanAmount}
            onChange={(event) => setLoanAmount(event.target.value)}
          />
        </label>
        <br />
        <label>
          Accounting Provider:
          <select
            value={accountingProvider}
            onChange={(event) => setAccountingProvider(event.target.value)}
          >
            <option value="">Select an accounting provider</option>
            <option value="Xero">Xero</option>
            <option value="MYOB">MYOB</option>
          </select>
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
      {decision && 
              <div>
              {
                  <div>
                      <p>BUSINESS NAME : {decision.business_name}</p>
                      <p>YEAR ESTABLISHED : {decision.year_established}</p>
                      <p>PRE ASSESSMENT : {decision.pre_assessment}</p>
                  </div>
              }
          </div>}
    </div>
  );
}

export default App;