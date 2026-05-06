import { useState } from "react";

type PredictionResult = {
  prediction: string;
  confidence: number;
  model: string;
  technique: string;
  accuracy: number;
};

function App() {
  const [news, setNews] = useState("");
  const [result, setResult] = useState<PredictionResult | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleCheckNews = async () => {
    setError("");
    setResult(null);

    if (!news.trim()) {
      setError(" Enter some news text first.");
      return;
    }

    try {
      setLoading(true);

      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          news: news,
        }),
      });

      const data = await response.json();

      if (data.error) {
        setError(data.error);
      } else {
        setResult(data);
      }
    } catch (err) {
      setError("Backend server is not running. Please start FastAPI backend.");
    } finally {
      setLoading(false);
    }
  };

  const handleExample = () => {
    setNews("Paste Here aonther News.");
  };

  const isFake = result?.prediction === "Fake News";

  return (
    <div className="min-h-screen bg-slate-100 px-4 py-10">
      <div className="mx-auto max-w-5xl">
        <div className="mb-8 text-center">
          <h1 className="text-3xl font-bold text-slate-900 md:text-5xl">
            Real / Fake Article Detection System
          </h1>
        </div>

        <div className="grid gap-6 md:grid-cols-3">
          <div className="rounded-2xl bg-white p-5 shadow-sm">
            <h2 className="text-lg font-semibold text-slate-900">Model</h2>
            <p className="mt-2 text-slate-600">Logistic Regression</p>
          </div>

          <div className="rounded-2xl bg-white p-5 shadow-sm">
            <h2 className="text-lg font-semibold text-slate-900">
              Feature Technique
            </h2>
            <p className="mt-2 text-slate-600">TF-IDF Vectorization</p>
          </div>

          <div className="rounded-2xl bg-white p-5 shadow-sm">
            <h2 className="text-lg font-semibold text-slate-900">Dataset</h2>
            <p className="mt-2 text-slate-600">Fake.csv + True.csv</p>
          </div>
        </div>

        <div className="mt-8 rounded-3xl bg-white p-6 shadow-sm md:p-8">
          <label className="mb-3 block text-lg font-semibold text-slate-900">
            Enter News Article
          </label>

          <textarea
            value={news}
            onChange={(e) => setNews(e.target.value)}
            placeholder="Paste or write news article here..."
            className="h-52 w-full resize-none rounded-2xl border border-slate-300 p-4 text-slate-800 outline-none transition focus:border-blue-500 focus:ring-4 focus:ring-blue-100"
          />

          {error && (
            <div className="mt-4 rounded-xl bg-red-50 p-4 text-red-600">
              {error}
            </div>
          )}

          <div className="mt-5 flex flex-col gap-3 sm:flex-row">
            <button
              onClick={handleCheckNews}
              disabled={loading}
              className="rounded-xl bg-blue-600 px-6 py-3 font-semibold text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-blue-300"
            >
              {loading ? "Analyzing..." : "Check News"}
            </button>

            <button
              onClick={handleExample}
              className="rounded-xl border border-slate-300 px-6 py-3 font-semibold text-slate-700 transition hover:bg-slate-100"
            >
              Try Example
            </button>
          </div>

          {loading && (
            <div className="mt-6 rounded-xl bg-blue-50 p-4 text-center text-blue-700">
              Please wait, the article is being analyzed...
            </div>
          )}

          {result && (
            <div
              className={`mt-8 rounded-2xl border p-6 ${
                isFake
                  ? "border-red-200 bg-red-50"
                  : "border-green-200 bg-green-50"
              }`}
            >
              <h2 className="text-xl font-bold text-slate-900">
                Prediction Result
              </h2>

              <p
                className={`mt-3 text-3xl font-bold ${
                  isFake ? "text-red-600" : "text-green-600"
                }`}
              >
                {result.prediction}
              </p>

              <div className="mt-5">
                <div className="mb-2 flex justify-between text-sm font-medium text-slate-700">
                  <span>Confidence</span>
                  <span>{result.confidence}%</span>
                </div>

                <div className="h-3 w-full rounded-full bg-slate-200">
                  <div
                    className={`h-3 rounded-full ${
                      isFake ? "bg-red-500" : "bg-green-500"
                    }`}
                    style={{ width: `${result.confidence}%` }}
                  ></div>
                </div>
              </div>

              <div className="mt-5 grid gap-3 text-sm text-slate-700 sm:grid-cols-3">
                <div className="rounded-xl bg-white p-3">
                  <strong>Model:</strong>
                  <br />
                  {result.model}
                </div>

                <div className="rounded-xl bg-white p-3">
                  <strong>Technique:</strong>
                  <br />
                  {result.technique}
                </div>

                <div className="rounded-xl bg-white p-3">
                  <strong>Accuracy:</strong>
                  <br />
                  {result.accuracy}%
                </div>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
