# Propresenter Pro 7 Reverse-Engineering

## Protobuffer

Propresenter 7 uses protocol buffers to save the presentation slide. 

For the protocol buffer, we have the entire message models in this git repository: [Link](https://github.com/greyshirtguy/ProPresenter7-Proto)


## Decode an example slide from binary (.pro file)

- Clone/Download git repository
- navigate inside "proto_7"
- enter this command (Make sure you select the correct .pro file for decoding)
```shell
protoc --decode rv.data.Presentation ./propresenter.proto < /Users/sebastiantatar/Documents/Work/BisericaEmanuel/ProPresenterPro7/conversion_pro7.pro > ../output.txt
```

## Change data

Now you can see the format. should look something like this: 

```
application_info {
  platform: PLATFORM_MACOS
  platform_version {
    major_version: 14
    minor_version: 4
  }
  application: APPLICATION_PROPRESENTER
  application_version {
    major_version: 7
    minor_version: 16
    patch_version: 1
    build: "118489346"
  }
}
uuid {
  string: "89507096-A0DD-450E-A534-08C585C6B2F1"
}
name: "conversion_pro7"
background {
}
chord_chart {
  platform: PLATFORM_MACOS
}
cue_groups {
  group {
    uuid {
      string: "D73B6D1B-966C-415B-A751-22C4AFF8B1D4"
    }
    hotKey {
    }
  }
  cue_identifiers {
    string: "3D2E30CB-F369-482E-AC98-D104658DAADA"
  }
  cue_identifiers {
    string: "4F5D6D02-C673-4307-8782-3F572553D84E"
  }
  cue_identifiers {
    string: "8326F15E-608E-44DB-A1D6-46D07BFF8FDF"
  }
}
```

In the cues, there is a property called RTF data. Change that at your will. (With python or whatever is needed)

## Encode the Text Format to binary

- Clone/Download git repository
- navigate inside "proto_7"
- enter this command (Make sure you select the correct .pro file for decoding)
```
protoc --encode=rv.data.Presentation ./propresenter.proto < /Users/sebastiantatar/Documents/Work/BisericaEmanuel/ProPresenterPro7/output.txt > ./../output.pro
```

