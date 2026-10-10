SmartStudy AI вЂ” starter project

This is a Flutter starter for an Android study/work helper app.

## Included
- Purple/white home screen
- Russian/English interface toggle
- Daily counter: 10 free tasks
- Daily reset based on device date
- Study, work, translator and topic-explainer entry points
- Placeholder flow for the future AI API
- Placeholder screen for rewarded ads

## Important: prototype, not production-ready
AI answers are NOT connected yet. Ads are NOT connected yet. The current daily limit is stored locally on the device and can be reset by reinstalling/clearing app data or manipulating device state. Before publishing, implement a secure backend for AI requests and quota enforcement, then integrate Google AdMob using its official Flutter SDK and test ad units.

## Run it
1. Install Flutter SDK and Android Studio.
2. In a terminal, run:
   `flutter create smartstudy_ai`
3. Replace the generated `pubspec.yaml` and `lib/main.dart` with the files in this archive.
4. Run:
   `flutter pub get`
   `flutter run`

## Before Google Play
- Configure the Android application ID and signing.
- Add a privacy policy and accurate Data safety disclosures.
- Complete current Google Play testing/account requirements.
- Integrate and test AI via a secure backend; never put private API keys in the app.
- Integrate AdMob and use test ads during development.
- Verify age rating, permissions, consent and advertising requirements.
