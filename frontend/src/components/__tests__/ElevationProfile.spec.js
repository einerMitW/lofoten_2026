import { describe, it, expect } from 'vitest';
import { mount } from '@vue/test-utils';
import ElevationProfile from '../ElevationProfile.vue';

describe('ElevationProfile.vue', () => {
  const sampleGeojson = {
    type: 'FeatureCollection',
    features: [
      {
        geometry: {
          coordinates: [
            [12.97, 67.87, 25.0],
            [12.98, 67.88, 150.0],
            [12.99, 67.89, 300.0]
          ]
        }
      }
    ]
  };

  const sampleTelemetry = {
    total_distance_km: 12.5,
    elevation_gain: 450,
    max_elevation: 300,
    min_elevation: 25
  };

  it('renders telemetry values correctly', () => {
    const wrapper = mount(ElevationProfile, {
      props: { geojson: sampleGeojson, telemetry: sampleTelemetry }
    });

    expect(wrapper.text()).toContain('12.5');
    expect(wrapper.text()).toContain('450');
    expect(wrapper.text()).toContain('300');
  });

  it('renders SVG paths when geojson is provided', () => {
    const wrapper = mount(ElevationProfile, {
      props: { geojson: sampleGeojson, telemetry: sampleTelemetry }
    });

    const pathElements = wrapper.findAll('path');
    expect(pathElements.length).toBe(2); // Area path and line path
  });
});
