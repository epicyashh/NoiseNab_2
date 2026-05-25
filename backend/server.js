require("dotenv").config();
const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
const PORT = process.env.PORT || 5001;

app.use(cors());
app.use(express.json());

mongoose
  .connect(process.env.MONGO_URI)
  .then(() => console.log("MongoDB Connected"))
  .catch((err) => console.error("MongoDB Connection Error:", err));

const noiseSchema = new mongoose.Schema(
  {
    City: { type: String, required: true },
    Place: { type: String, required: true },
    "Noise level(dB)": { type: Number, required: true },
    Category: { type: String, required: true },
  },
  { collection: "NoiseCollection" }
);

const NoiseReport = mongoose.model("NoiseReport", noiseSchema);

app.get("/api/health", (req, res) => {
  res.json({ status: "ok" });
});

app.post("/api/noise/report", async (req, res) => {
  try {
    const { city, place, noise_level, category } = req.body;

    const newReport = new NoiseReport({
      City: city,
      Place: place,
      "Noise level(dB)": noise_level,
      Category: category,
    });

    await newReport.save();
    res.status(201).json({ message: "Noise data saved successfully!" });
  } catch (error) {
    console.error("Error saving noise data:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
